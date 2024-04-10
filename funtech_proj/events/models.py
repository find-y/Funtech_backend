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


class Event(models.Model):
    # поля сгруппированы по типу
    # данные проставляются автоматически
    org = models.ForeignKey(
        User,
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
        Town,
        on_delete=models.PROTECT,
        verbose_name="Город",
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.PROTECT,
        verbose_name="Формат",
    )

    # участник выбирает несколько из списка. или добавляет свое
    participants = models.ManyToManyField(
        User,
        through="ParticipantEvent",
        # verbose_name='Участники',
    )
    specializations = models.ManyToManyField(
        Specialization,
        # through="SpecializationEvent",
        # verbose_name='Участники',
    )
    stacks = models.ManyToManyField(
        Stack,
        # through="StackEvent",
        # verbose_name='Участники',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"
        ordering = ("date",)


class Gallery_image(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="gallery_images",
        # verbose_name='Ивент'
    )
    image = models.ImageField(
        # verbose_name="Изображение галереи",
        # verbose_name_plural="Изображения галереи",
        upload_to="events/images/gallery_images/",
        validators=(v.validate_image_file_extension,),
    )

    class Meta:
        verbose_name = "Изображение для галереи"
        verbose_name_plural = "Галерея изображений"
        ordering = ("event",)


class Speaker(models.Model):
    name = models.CharField(
        "ФИО",
        max_length=256,
        # related_name="speaker_event",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="speakers",
        # related_name="speakers_events",
        # verbose_name='Ивент'
    )
    position = models.CharField(max_length=256, verbose_name="Должность")
    photo = models.ImageField(
        # verbose_name="Изображение галереи",
        # verbose_name_plural="Изображения галереи",
        upload_to="events/images/speakers_photos/",
        validators=(v.validate_image_file_extension,),
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ("event",)


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
        ordering = ("name",)


class ParticipantEvent(models.Model):
    # можно унаследовать от кастом юзера
    # если хотим записывать сюда текущую анкету без привязки к профилю
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="participated_events",
        verbose_name="Участник ивента",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        related_name="participated_events",
        # verbose_name='Ивент'
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
