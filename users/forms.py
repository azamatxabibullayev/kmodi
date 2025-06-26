from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your password')
        }),
        label=_("Password")
    )

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your full name')
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your phone number')
            }),
        }
        labels = {
            'full_name': _("Full Name"),
            'phone': _("Phone Number"),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Phone number"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Password"))


class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label=_("Password")
    )

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'email', 'password']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': _('Phone number')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Your email address')}),
        }
        labels = {
            'full_name': _("Full Name"),
            'phone': _("Phone Number"),
            'email': _("Email Address"),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.exclude(pk=self.instance.pk).filter(email=email)
            if qs.exists():
                raise forms.ValidationError(_("This email is already in use."))
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            qs = User.objects.exclude(pk=self.instance.pk).filter(phone=phone)
            if qs.exists():
                raise forms.ValidationError(_("This phone number is already in use."))
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
