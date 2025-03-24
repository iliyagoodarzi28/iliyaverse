from django import forms




class ResumeFilterForm(forms.Form):
    FILTER_CHOICES = [
        ('most_viewed', 'پر بازدیدترین'),
        ('latest', 'جدید ترین'),
        ('oldest', 'قدیمی ترین'),
        
    ]
    
    filter_by = forms.ChoiceField(choices=FILTER_CHOICES, label="فیلتر")