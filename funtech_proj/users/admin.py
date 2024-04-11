from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class BaseAdmin(admin.ModelAdmin):
    """Базовый класс для настроек административного интерфейса."""

    empty_value_display = "-"
    list_per_page = 20


@admin.register(User)
class UserAdminPanel(UserAdmin):
    """Класс для настройки административного интерфейса пользователей."""

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "mobilefone",
        "workplace",
        "position",
        "experience",
    )
    list_filter = (
        "username",
        "first_name",
        "last_name",
        "email",
        "mobilefone",
        "workplace",
        "position",
        "experience",
    )
    search_fields = (
        "username",
        "email",
    )
    ordering = ("username",)
