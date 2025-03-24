from django.contrib import admin
from .models import CategoryResume, Resume , Skill

class CategoryResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # نمایش نام و توضیحات در لیست
    search_fields = ('name',)  # امکان جستجو بر اساس نام

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')  # نمایش عنوان، دسته‌بندی و تاریخ‌ها
    list_filter = ('category',)  # فیلتر بر اساس دسته‌بندی
    search_fields = ('title', 'content')  # امکان جستجو بر اساس عنوان و محتوا


# ثبت مدل‌ها در پنل ادمین
admin.site.register(CategoryResume, CategoryResumeAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Skill)