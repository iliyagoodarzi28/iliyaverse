from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'), 
    path('resumes/', views.ResumeListView.as_view(), name='resume_list'),
    path('resume/<slug:slug>/', views.ResumeDetailView.as_view(), name='resume_detail'),

]