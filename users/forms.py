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


class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'email', 'password']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon raqam'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email manzilingiz'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.exclude(pk=self.instance.pk).filter(email=email)
            if qs.exists():
                raise forms.ValidationError("Bu email allaqachon mavjud.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            qs = User.objects.exclude(pk=self.instance.pk).filter(phone=phone)
            if qs.exists():
                raise forms.ValidationError("Bu telefon raqam allaqachon mavjud.")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
