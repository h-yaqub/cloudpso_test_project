# Generated by Django 3.0 on 2023-12-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=30, verbose_name="Full Name"),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=254,
                        unique=True,
                        verbose_name="Email Address",
                    ),
                ),
                ("username", models.CharField(max_length=100, verbose_name="Username")),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Staff Member"),
                ),
                (
                    "date_joined",
                    models.DateField(auto_now_add=True, verbose_name="Registered At"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
