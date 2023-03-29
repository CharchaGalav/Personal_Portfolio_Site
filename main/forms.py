from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
    
    name = forms.CharField(max_length=200, required=True,
         widget=forms.TextInput(attrs={
        'placeholder': 'Your Full Name',
        'class': 'form-control'
        }))
    
    email = forms.EmailField(max_length=200, required=True,
        widget=forms.TextInput(attrs={
        'placeholder': 'Email Address',
        'class': 'form-control'
        }))
    
    message = forms.CharField( required=True,
            widget=forms.Textarea(attrs={
        'placeholder': 'Your Message...',
        'class': 'form-control'
        }))



