from django.db import models
import jdatetime
from django.utils.text import slugify
from django_summernote.fields import SummernoteTextField
from ckeditor.fields import RichTextField


class CategoryResume(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='your_default_value', null=False , unique=True)


    class Meta:
        ordering = ('name',)

        
    def __str__(self):
        return self.name

class Resume(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Add this line
    content = RichTextField(blank=True , null=True)
    category = models.ForeignKey(CategoryResume, on_delete=models.CASCADE, related_name='resumes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_one = models.ImageField(upload_to='resume/%Y/%m/%d', blank=True)
    views = models.PositiveIntegerField(default=0) 
    skills = models.ManyToManyField('Skill', related_name='resumes', blank=True)  # Add this line



    def __str__(self):
        return self.title

    def get_persian_date(self):
        # تبدیل تاریخ میلادی به تاریخ شمسی
        persian_date = jdatetime.datetime.fromgregorian(datetime=self.created_at)
        return persian_date.strftime('%Y/%m/%d')


class Skill(models.Model):
    content =models.TextField( blank=True, null=True, verbose_name="مهارت ها")

def __str__(self):
    return self.content
