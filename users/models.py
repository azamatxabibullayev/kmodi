from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    def create_user(self, full_name=None, phone=None, password=None, email=None, role='student', **extra_fields):
        if not phone and not email:
            raise ValueError("Telefon raqam yoki email bo‘lishi shart")

        if not full_name:
            full_name = email or phone or "Foydalanuvchi"

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
        ('student', 'Talaba'),
        ('admin', 'Admin'),
    )
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"

    @property
    def is_staff(self):
        return self.is_admin
