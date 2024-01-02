from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email is required.")

        if not password:
            raise ValueError("Password is required.")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.username = username
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError("Email is required.")

        if not password:
            raise ValueError("Password is required.")

        user = self.create_user(email, username, password)
        user.username = username
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField("Full Name", max_length=30)
    email = models.EmailField("Email Address", unique=True, db_index=True)
    username = models.CharField("Username", max_length=100)
    is_active = models.BooleanField("Active", default=True)
    is_staff = models.BooleanField("Staff Member", default=False)
    date_joined = models.DateField("Registered At", auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class AppPermission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    permissions = models.ManyToManyField(AppPermission)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_notes"
    )
    assigned_to = models.ManyToManyField(User, related_name="assigned_notes")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
