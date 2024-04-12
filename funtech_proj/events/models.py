# from users.models import User
from django.conf import settings
from django.core import validators as v
from django.db import models
from shared import models as m


class Event(models.Model):
    # поля сгруппированы по типу
    # данные проставляются автоматически
    org = models.ForeignKey(
        # User,
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Организатор",
        related_name="organized_events",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    # орг ставит галочку или нет
    registration_open = models.BooleanField(verbose_name="Регистрация открыта")

    # орг вводит свое значение
    date = models.DateField(verbose_name="Дата проведения")
    head_image = models.ImageField(
        verbose_name="Основное изображение",
        upload_to="events/images/head_images/",
        validators=(v.validate_image_file_extension,),
    )
    name = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    address = models.TextField(verbose_name="Адрес")
    video_link = models.URLField(  # трансляция и запись будут по одной ссылке?
        max_length=256, verbose_name="Видео линк"
    )
    # program = models.TextField(verbose_name="Программа")
    # простой вариант, если фронт не будет успевать

    # орг вводит список своих значений (прописано в связных моделях)
    # program_parts
    # gallery_images
    # speakers

    # участник выбирает одно из списка. или добавляет свое
    town = models.ForeignKey(
        m.Town,
        on_delete=models.PROTECT,
        verbose_name="Город",
    )
    form = models.ForeignKey(
        m.Form,
        on_delete=models.PROTECT,
        verbose_name="Формат",
    )

    # участник выбирает несколько из списка. или добавляет свое
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="ParticipantEvent",
        verbose_name="Участники",
    )
    specializations = models.ManyToManyField(
        m.Specialization,
        verbose_name="Направления",
        related_name="events",
    )
    stacks = models.ManyToManyField(
        m.Stack,
        verbose_name="Стэк",
        related_name="events",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ("date",)


class Gallery_image(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="gallery_images",
        verbose_name="Мероприятие",
    )
    image = models.ImageField(
        verbose_name="Изображение галереи",
        upload_to="events/images/gallery_images/",
        validators=(v.validate_image_file_extension,),
    )

    class Meta:
        verbose_name = "Изображение для галереи"
        verbose_name_plural = "Галерея изображений"
        ordering = ("event",)


class Speaker(models.Model):
    name = models.CharField("ФИО", max_length=256)
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="speakers",
        # related_name="speakers_events",
        verbose_name="Мероприятие",
    )
    position = models.CharField(max_length=256, verbose_name="Должность")
    photo = models.ImageField(
        verbose_name="Фото докладчика",
        upload_to="events/images/speakers_photos/",
        validators=(v.validate_image_file_extension,),
    )

    class Meta:
        verbose_name = "Докладчик"
        verbose_name_plural = "Докладчики"
        ordering = ("event",)


class Program_part(m.TemplateName):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="Мероприятие",
    )
    time = models.TimeField("Время проведения")

    class Meta:
        verbose_name = "Часть программы"
        verbose_name_plural = "Части программы"
        ordering = ("name",)


class ParticipantEvent(models.Model):
    # можно унаследовать от кастом юзера
    # если хотим записывать сюда текущую анкету без привязки к профилю
    participant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="participated_events",
        verbose_name="Участник мероприятия",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="participated_events",
        verbose_name="Мероприятие",
    )
    participate_online = models.BooleanField(
        verbose_name="Участвую онлайн", default=False
    )
    agreement_events = models.BooleanField(
        verbose_name="Соглашаюсь получать приглашения", default=False
    )
    agreement_vacancies = models.BooleanField(
        verbose_name="Соглашаюсь получать вакансии", default=False
    )
    # это должно быть на фронте
    # update_profile = models.BooleanField(verbose_name="Обновить мой профиль")

    class Meta:
        verbose_name = "Участник Ивента"
        verbose_name_plural = "Участники Ивентов"
        ordering = ("event",)
