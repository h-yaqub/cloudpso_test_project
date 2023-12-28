from django.contrib import admin

from core import models


@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(models.UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "created_at", "updated_at")
    search_fields = ("user__username", "user__email")
