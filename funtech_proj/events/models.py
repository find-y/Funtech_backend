from django.db import models

from users.models import User


class TemplateName(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('-name',)


class Town(TemplateName):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Galery_image(TemplateName):
    class Meta:
        verbose_name = 'Изображений для галереи'
        verbose_name_plural = 'Галерея изображений'


class Speaker(TemplateName):
    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'


class Program_part(TemplateName):
    class Meta:
        verbose_name = 'Часть программы'
        verbose_name_plural = 'Части программы'


class Tag(TemplateName):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Ключевые навыки'


class Event(models.Model):
# поля сгруппированы по типу
    # данные проставляются автоматически
    org = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Организатор',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    # орг ставит галочку или нет
    registration_open = models.BooleanField(
        verbose_name='Регистрация открыта')

    # орг вводит свое значение
    date = models.DateTimeField(
        verbose_name='Дата проведения')
    head_image = models.ImageField(
        verbose_name='Основное изображение')
    name = models.CharField(
        max_length=256,
        verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание')
    address = models.TextField(
        verbose_name='Адрес')
    video = models.CharField( #трансляция и запись будут по одной ссылке?
        max_length=256,
        verbose_name='Видео')

    # участник выбирает одно из списка. или добавляет свое
    town = models.ForeignKey(
        Town,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name='Город',
    )

    # участник выбирает несколько из списка. или добавляет свое
    galery_images = models.ManyToManyField(
        Galery_image,
        through='Galery_imageEvent',
        # verbose_name='Галерея изображений',
    )
    speakers = models.ManyToManyField(
        Speaker,
        through='SpeakerEvent',
        # verbose_name='Спикеры',
    )
    program_parts = models.ManyToManyField(
        Program_part,
        through='Program_partEvent',
        # verbose_name='Части программы',
    )
    participants = models.ManyToManyField(
        User,
        through='UsesEvent',
        # verbose_name='Участники',
    )
    tags = models.ManyToManyField(
        Tag,
        through='TagEvent',
        # verbose_name='Теги',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'
        ordering = ('date',)


class Galery_imageEvent(models.Model):
    galery_image = models.ForeignKey(
        Galery_image,
        on_delete=models.CASCADE,
        # verbose_name='Изображение для галереи'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        # verbose_name='Ивент'
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ('event',)


class SpeakerEvent(models.Model):
    speaker = models.ForeignKey(
        Speaker,
        on_delete=models.CASCADE,
        # verbose_name='Изображение для галереи'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        # verbose_name='Ивент'
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ('event',)


class Program_partEvent(models.Model):
    program_part = models.ForeignKey(
        Program_part,
        on_delete=models.CASCADE,
        # verbose_name='Изображение для галереи'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        # verbose_name='Ивент'
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ('event',)


class ParticipantEvent(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # verbose_name='Изображение для галереи'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        # verbose_name='Ивент'
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ('event',)


class TagEvent(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        # verbose_name='Изображение для галереи'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.PROTECT,
        # verbose_name='Ивент'
    )

    class Meta:
        # verbose_name = 'Заявка-Навык'
        # verbose_name_plural = 'Заявки-Навыки'
        ordering = ('event',)
