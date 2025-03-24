from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),  # لیست مقالات
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),  # جزئیات مقاله
    path('categories/', views.CategoryListView.as_view(), name='blog_category_list'),  # لیست دسته‌بندی‌ها
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='blog_category_detail'), 
    path('comment/edit/<int:pk>/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
    
]
