from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Specialization, Stack

# внес шаблонного кастомного юзера из заготовок,
# чтобы можно было тестировать модели ивентов


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "username",
        "first_name",
        "last_name",
    )

    email = models.EmailField(
        verbose_name="Электронная почта",
        unique=True,
    )
    username = models.CharField(
        verbose_name="Юзернейм",
        unique=True,
        max_length=25,
    )
    first_name = models.CharField(
        verbose_name="Имя пользователя",
        max_length=25,
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя",
        max_length=25,
    )
    password = models.CharField(
        verbose_name="Пароль",
        max_length=25,
    )
    stack = models.ManyToManyField(
        Stack,
        related_name="users",
        blank=True,
    )
    specialization = models.ManyToManyField(
        Specialization, related_name="users", blank=True
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
