from django.views.generic import TemplateView
from site_info.models import SiteInfo
from blog.models import Blog

class BaseSiteInfoView(TemplateView):
    """Base view to include site information in context."""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_info'] = SiteInfo.get_info()
        return context
    
    
class HomeView(BaseSiteInfoView):
    template_name = 'home/index.html'  # قالب صفحه خانه

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # گرفتن ۳ بلاگ آخرین، مرتب‌شده بر اساس تاریخ
        context['latest_posts'] = Blog.objects.all().order_by('-date')[:3]
        return context



class AboutView(BaseSiteInfoView):
    template_name = 'home/about.html'


    




# views.py
from django.shortcuts import render, get_object_or_404
from blog.models import Category
from resume.models import CategoryResume

def combined_category_view(request):
    # Fetch categories from both models
    categories = Category.objects.all()[:2]  # Fetch two categories from the Blog
    categories_resume = CategoryResume.objects.all()[:2]  # Fetch two categories from Resume
    return render(request, 'home/combined_category.html', {
        'categories': categories,
        'categories_resume': categories_resume
    })

# views.py

def combined_category_detail_view(request, blog_slug, resume_slug):

    blog_category = get_object_or_404(Category, slug=blog_slug)
    blogs = blog_category.blogs.all()

    resume_category = get_object_or_404(CategoryResume, slug=resume_slug)
    resumes = resume_category.resumes.all()

    return render(request, 'home/combined_category_detail.html', {
        'blog_category': blog_category,
        'blogs': blogs,
        'resume_category': resume_category,
        'resumes': resumes
    })

