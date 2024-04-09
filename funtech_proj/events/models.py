from django.core import validators as v
from django.db import models
from users.models import User


class TemplateName(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ("name",)


class Town(TemplateName):
    class Meta(TemplateName.Meta):
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Form(TemplateName):
    class Meta(TemplateName.Meta):
        verbose_name = "Формат"
        verbose_name_plural = "Формат"


class Speaker(TemplateName):
    class Meta(TemplateName.Meta):
        verbose_name = "Спикер"
        verbose_name_plural = "Спикеры"


class Theme(TemplateName):
    class Meta(TemplateName.Meta):
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Specialization(TemplateName):
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        verbose_name="Тема",
    )

    class Meta(TemplateName.Meta):
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Stack(TemplateName):
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        verbose_name="Направление",
    )

    class Meta(TemplateName.Meta):
        verbose_name = "Стэк"
        verbose_name_plural = "Стэк"


class Gallery_image(models.Model):
    image = models.ImageField(
        upload_to="events/images/",
        validators=(v.validate_image_file_extension,),
    )

    class Meta:
        verbose_name = "Изображение для галереи"
        verbose_name_plural = "Галерея изображений"


class Event(TemplateName):
    name = models.CharField(max_length=256, verbose_name="Название")
    org = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Организатор",
        related_name="organized_events",
    )
    # участник выбирает одно из списка. или добавляет свое
    town = models.ForeignKey(
        Town,
        on_delete=models.CASCADE,  # добавить: при вводе букв - подсказки
        verbose_name="Город",
    )
    head_image = models.ForeignKey(
        Gallery_image,
        related_name="head_image_of_events",
        on_delete=models.PROTECT,
        verbose_name="Основное изображение",
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name="Формат",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    date = models.DateTimeField(verbose_name="Дата проведения")
    registration_open = models.BooleanField(verbose_name="Регистрация открыта")
    description = models.TextField(verbose_name="Описание")
    address = models.TextField(verbose_name="Адрес")
    video = models.URLField(  # трансляция и запись будут по одной ссылке?
        max_length=256, verbose_name="Видео линк"
    )
    # участник выбирает несколько из списка. или добавляет свое
    gallery_images = models.ManyToManyField(Gallery_image)
    speakers = models.ManyToManyField(Speaker)
    specializations = models.ManyToManyField(Specialization)
    stack = models.ManyToManyField(Stack)
    participants = models.ManyToManyField(
        User,
        through="ParticipantEvent",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"
        ordering = ("date",)


class Program_part(TemplateName):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="Ивент",
    )
    time = models.TimeField()

    class Meta:
        verbose_name = "Часть программы"
        verbose_name_plural = "Части программы"
        ordering = ("event",)


class ParticipantEvent(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="participated_events",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="participated_events",
    )
    participate_online = models.BooleanField(verbose_name="Участвую онлайн")
    agreement_events = models.BooleanField(
        verbose_name="Соглашаюсь получать приглашения"
    )
    agreement_vacancies = models.BooleanField(
        verbose_name="Соглашаюсь получать вакансии"
    )
    # это должно быть на фронте
    # update_profile = models.BooleanField(verbose_name="Обновить мой профиль")

    class Meta:
        verbose_name = "Участник Ивента"
        verbose_name_plural = "Участники Ивентов"
        ordering = ("event",)
