from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('categories/', views.combined_category_view, name='combined_category_view'),
    path('category/<slug:blog_slug>/<slug:resume_slug>/', views.combined_category_detail_view, name='combined_category_detail'),



    

]