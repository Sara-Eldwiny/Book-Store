

from django import forms
from .models import Author
from .models import new_book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'image', 'birth_date']  
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }





class BookForm(forms.ModelForm):
    class Meta:
        model = new_book
        fields = ['name', 'author', 'price', 'pages', 'image']  
