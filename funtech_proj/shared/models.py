from django.db import models


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
        verbose_name_plural = "Форматы"


class Theme(TemplateName):
    class Meta(TemplateName.Meta):
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Specialization(TemplateName):
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        verbose_name="Тема",
        related_name="specializations",
    )

    class Meta(TemplateName.Meta):
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Stack(TemplateName):
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        verbose_name="Направление",
        related_name="stacks",
    )

    class Meta(TemplateName.Meta):
        verbose_name = "Стэк"
        verbose_name_plural = "Стэк"
