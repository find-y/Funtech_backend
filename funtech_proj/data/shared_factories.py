from class_makers.db_preload import template_name_class_maker
from factory import Sequence, SubFactory
from factory.django import DjangoModelFactory
from shared.models import Form, Specialization, Stack, Theme, Town

TownFactory = template_name_class_maker(Town, "Город")
FormFactory = template_name_class_maker(Form, "Формат")
ThemeFactory = template_name_class_maker(Theme, "Тема")


class SpecializationFactory(DjangoModelFactory):
    class Meta:
        model = Specialization

    name = Sequence(lambda n: f"Направление №{n}")
    theme = SubFactory(ThemeFactory)


class StackFactory(DjangoModelFactory):
    class Meta:
        model = Stack

    name = Sequence(lambda n: f"Стэк №{n}")
    specialization = SubFactory(SpecializationFactory)
