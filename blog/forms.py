# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'content': 'متن نظر',
        }


class BlogFilterForm(forms.Form):
    FILTER_CHOICES = [
        ('most_viewed', 'پر بازدیدترین'),
        ('latest', 'جدید ترین'),
        ('oldest', 'قدیمی ترین'),
        
    ]
    
    filter_by = forms.ChoiceField(choices=FILTER_CHOICES, label="فیلتر بلاگ")