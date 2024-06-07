from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 
from django.contrib.auth.models import User # imports database model for user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'py-4 px-6 rounded-xl w-full',
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'py-4 px-6 rounded-xl w-full',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'py-4 px-6 rounded-xl w-full',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-enter password',
        'class': 'py-4 px-6 rounded-xl w-full',
    }))