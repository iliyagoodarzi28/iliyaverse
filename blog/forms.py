# forms.py
from django import forms
from .models import Comment , Rating

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



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.Select(choices=[(i, i) for i in range(1, 6)])  # انتخاب امتیاز از 1 تا 5
        }    