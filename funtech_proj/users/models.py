from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "username",
        "first_name",
        "last_name",
        "mobilefone",
        "workplace",
        "position",
        "experience",
    )
    EXPERIENCE_CHOICES = [
        ("", ""),
        ("BEGINNER", "От 1 года"),
        ("INTERMEDIATE", "От 3 лет"),
        ("ADVANCED", "ОТ 5 лет"),
        ("Other", "Другое"),
    ]

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
    mobilefone = models.CharField(
        verbose_name="Мобильный телефон",
        unique=True,
        max_length=15,
    )
    workplace = models.CharField(
        verbose_name="Место работы",
        max_length=25,
    )
    position = models.CharField(
        verbose_name="Должность",
        unique=True,
        max_length=15,
    )
    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
