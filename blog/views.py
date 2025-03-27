from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Blog, Category, Comment
from django.db.models import Q
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm, BlogFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
import markdown



def latest_posts(request):
    posts = Blog.objects.all().order_by('-created_at')[:3]  # آخرین ۳ مقاله
    return posts

class BlogView(View):
    def get(self, request):
        form = BlogFilterForm(request.GET or None)
        blogs = Blog.objects.all()  # Default to all blogs

        if form.is_valid():
            filter_choice = form.cleaned_data['filter_by']
            filter_map = {
                'most_viewed': '-views',
                'latest': '-date',
                'oldest': 'date'
            }
            blogs = blogs.order_by(filter_map.get(filter_choice, 'date'))

        search_query = request.GET.get('q')
        if search_query:
            blogs = blogs.filter(
                Q(name__icontains=search_query) |
                Q(slug__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return render(request, 'blog/blog.html', {
            'blogs': blogs,
            'form': form
        })


class BlogDetailView(View):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        blog.views += 1
        blog.save()
        comments = blog.comments.all()
        form = CommentForm()
        return render(request, 'blog/blog_detail.html', {
            'blog': blog,
            'comments': comments,
            'form': form
        })

    def post(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        
        # بررسی اینکه آیا کاربر وارد شده است یا خیر
        if not request.user.is_authenticated:
            return render(request, 'accounts/login_prompt.html', {
                'message': "شما ثبت نام نکرده‌اید. آیا می‌خواهید ثبت‌نام کنید یا وارد شوید؟"
            })

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user  # تنظیم کاربر
            comment.save()
            return redirect('blog_detail', slug=blog.slug)

        comments = blog.comments.all()
        return render(request, 'blog/blog_detail.html', {
            'blog': blog,
            'comments': comments,
            'form': form
        })

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    login_url = 'login'  # URL صفحه ورود

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'slug': self.object.blog.slug})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    login_url = 'login'  # URL صفحه ورود

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'slug': self.object.blog.slug})
    

class CategoryListView(ListView):
    model = Category
    template_name = 'home/combined_category.html'
    context_object_name = 'categories'


class CategoryDetailView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        blogs = category.blogs.all()
        return render(request, 'home/combined_category_detail.html', {
            'category': category,
            'blogs': blogs
        })