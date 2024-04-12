from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import Specialization, Stack

MAX_LENGTH = 255
PHONE_NUMBER_MAX_LENGTH = 25
FIELD_NOT_REQUIRED = settings.FIELD_NOT_REQUIRED


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)
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
        max_length=MAX_LENGTH,
    )
    username = models.CharField(
        verbose_name="Юзернейм",
        unique=True,
        max_length=MAX_LENGTH,
    )
    password = models.CharField(
        verbose_name="Пароль",
        max_length=MAX_LENGTH,
    )
    first_name = models.CharField(
        verbose_name="Имя пользователя",
        max_length=MAX_LENGTH,
        **FIELD_NOT_REQUIRED,
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя",
        max_length=MAX_LENGTH,
        **FIELD_NOT_REQUIRED,
    )
    mobilefone = models.CharField(
        verbose_name="Мобильный телефон",
        max_length=PHONE_NUMBER_MAX_LENGTH,
        **FIELD_NOT_REQUIRED,
    )
    workplace = models.CharField(
        verbose_name="Место работы",
        max_length=MAX_LENGTH,
        **FIELD_NOT_REQUIRED,
    )
    position = models.CharField(
        verbose_name="Должность",
        max_length=MAX_LENGTH,
        **FIELD_NOT_REQUIRED,
    )
    experience = models.CharField(
        max_length=MAX_LENGTH,
        choices=EXPERIENCE_CHOICES,
        **FIELD_NOT_REQUIRED,
    )
    stacks = models.ManyToManyField(
        Stack,
        related_name="users",
        blank=True,
    )
    specializations = models.ManyToManyField(
        Specialization,
        related_name="users",
        blank=True,
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
