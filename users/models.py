from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, full_name=None, phone=None, password=None, email=None, role='student', **extra_fields):
        if not phone and not email:
            raise ValueError(_("Phone number or email is required"))

        if not full_name:
            full_name = email or phone or _("User")

        user = self.model(
            full_name=full_name,
            phone=phone,
            email=email,
            role=role,
            **extra_fields
        )
        user.set_password(password or get_random_string(12))
        user.save()
        return user

    def create_superuser(self, full_name, phone, password, email=None):
        user = self.create_user(
            full_name=full_name,
            phone=phone,
            password=password,
            email=email,
            role='admin'
        )
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('student', _("Student")),
        ('admin', _("Admin")),
    )
    full_name = models.CharField(_("Full Name"), max_length=100)
    phone = models.CharField(_("Phone Number"), max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(_("Email Address"), unique=True, null=True, blank=True)
    role = models.CharField(_("Role"), max_length=10, choices=ROLE_CHOICES, default='student')
    is_active = models.BooleanField(_("Active"), default=True)
    is_admin = models.BooleanField(_("Admin"), default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"

    @property
    def is_staff(self):
        return self.is_admin
