from django.db import models
from django.urls import reverse
from django.utils import timezone
import jdatetime
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name    

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    description = RichTextField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug,]) 

    def get_persian_date(self):
        # تبدیل تاریخ میلادی به تاریخ شمسی
        persian_date = jdatetime.datetime.fromgregorian(datetime=self.date)
        return persian_date.strftime('%Y/%m/%d')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog}'

    def get_persian_created_at(self):
        # تبدیل تاریخ میلادی به تاریخ شمسی
        persian_date = jdatetime.datetime.fromgregorian(datetime=self.created_at)
        return persian_date.strftime('%Y/%m/%d')