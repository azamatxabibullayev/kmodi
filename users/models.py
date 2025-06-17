from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, full_name, phone, password=None, role='student'):
        if not phone:
            raise ValueError("Telefon raqam kiritilishi shart")
        user = self.model(full_name=full_name, phone=phone, role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, full_name, phone, password):
        user = self.create_user(full_name, phone, password, role='admin')
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
    phone = models.CharField(max_length=20, unique=True)
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
