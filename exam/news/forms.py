from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm) :
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'article', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Title name'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'             
            }), 
            "article": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
        }