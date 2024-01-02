from .models import AppPermission


def accessible_permissions(request):
    permissions = []

    if request.user.is_authenticated:
        if request.user.is_superuser:
            permissions.extend(
                list(AppPermission.objects.all().values_list("name", flat=True))
            )
        else:
            for user_role in request.user.roles.all():
                permissions.extend(
                    list(
                        user_role.role.permissions.all().values_list("name", flat=True)
                    )
                )

    return {"allowed_permissions": permissions}
