from datetime import datetime as dt

import factory as f
from class_makers.db_preload import template_name_class_maker
from events import models as m
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = f.Sequence(lambda n: f"Username_{n}")
    email = f.LazyAttribute(lambda _self: f"{_self.username.lower()}@example.com")
    password = f.Faker("password")


TownFactory = template_name_class_maker(m.Town, "Город")
FormFactory = template_name_class_maker(m.Form, "Формат")
ThemeFactory = template_name_class_maker(m.Theme, "Тема")


class SpecializationFactory(DjangoModelFactory):
    class Meta:
        model = m.Specialization

    name = f.Sequence(lambda n: f"Направление №{n}")
    theme = f.SubFactory(ThemeFactory)


class StackFactory(DjangoModelFactory):
    class Meta:
        model = m.Stack

    name = f.Sequence(lambda n: f"Стэк №{n}")
    specialization = f.SubFactory(SpecializationFactory)


class EventFactory(DjangoModelFactory):
    class Meta:
        model = m.Event

    registration_open = f.LazyAttribute(lambda _self: _self.date >= dt.now().date())

    org = f.SubFactory(UserFactory)
    town = f.SubFactory(TownFactory)
    form = f.SubFactory(FormFactory)

    date = f.Faker("date_this_year", after_today=True)
    head_image = f.django.ImageField()
    name = f.Sequence(lambda n: f"Ивент №{n}")
    description = f.Faker("text")
    address = f.Faker("address")
    video_link = f.Faker("url")

    @f.post_generation
    def specializations(self, create, extracted, **kwargs):
        if create and extracted:
            self.specializations.add(*extracted)

    @f.post_generation
    def stacks(self, create, extracted, **kwargs):
        if create and extracted:
            self.stacks.add(*extracted)


class Gallery_imageFactory(DjangoModelFactory):
    class Meta:
        model = m.Gallery_image

    event = None
    image = f.django.ImageField()


class SpeakerFactory(DjangoModelFactory):
    class Meta:
        model = m.Speaker

    name = f.Sequence(lambda n: f"ФИО №{n}")
    event = None
    position = f.Faker("job")
    photo = f.django.ImageField()


class Program_partFactory(DjangoModelFactory):
    class Meta:
        model = m.Program_part

    name = f.Sequence(lambda n: f"Часть программы №{n}")
    event = None
    time = f.Faker("time_object")


class ParticipantEventFactory(DjangoModelFactory):
    class Meta:
        model = m.ParticipantEvent

    participant = None
    event = None
    participate_online = f.Iterator((True, False))
    agreement_events = f.Iterator((True, False))
    agreement_vacancies = f.Iterator((True, False))
