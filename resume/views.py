from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import CategoryResume, Resume
from django.db.models import Q
from .forms import ResumeFilterForm

class CategoryListView(ListView):
    model = CategoryResume
    template_name = 'home/combined_category.html'
    context_object_name = 'categories'


class CategoryDetailView(View):
    def get(self, request, slug):
        category = get_object_or_404(CategoryResume, slug=slug)
        resumes = category.resumes.all()
        return render(request, 'home/combined_category_detail.html', {
            'category': category,
            'resumes': resumes
        })


class ResumeListView(View):
    def get(self, request):
        # Initialize with all resumes
        resumes = Resume.objects.all()
        
        # Handle filtering
        form = ResumeFilterForm(request.GET or None)
        if form.is_valid():
            filter_choice = form.cleaned_data['filter_by']
            filter_map = {
                'most_viewed': '-views',
                'latest': '-created_at',
                'oldest': 'created_at'
            }
            resumes = resumes.order_by(filter_map.get(filter_choice, '-created_at'))  # Default to latest
        
        # Handle search
        search_query = request.GET.get('q')
        if search_query:
            resumes = resumes.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        
        # Render template with both resumes and form
        context = {
            'resumes': resumes,
            'form': form
        }
        return render(request, 'resume/resume_list.html', context)


class ResumeDetailView(View):
    def get(self, request, slug):
        # Retrieve the resume object based on the slug
        resume = get_object_or_404(Resume, slug=slug)
        resume.views += 1
        resume.save()  # اصلاح شده: اضافه کردن پرانتز برای فراخوانی متد save
        
        # Render the template with the resume object
        context = {
            'resume': resume
        }
        return render(request, 'resume/resume_detail.html', context)