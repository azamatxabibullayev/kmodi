from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol kiriting'
    }))

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'To‘liq ismingiz'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqamingiz'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Telefon raqam")
    password = forms.CharField(widget=forms.PasswordInput)
