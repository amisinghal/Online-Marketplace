from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields= ('username', 'email', 'password1', 'password2')

    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your Username',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))
    
    email= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your email id',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))

    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat-password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))