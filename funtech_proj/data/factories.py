from datetime import datetime as dt

import factory as f
from events import models as m
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = f.Sequence(lambda n: f"Username_{n}")
    email = f.LazyAttribute(lambda _self: f"{_self.username.lower()}@example.com")
    password = f.Faker("password")


class TownFactory(DjangoModelFactory):
    class Meta:
        model = m.Town

    name = f.Sequence(lambda n: f"Город №{n}")


class FormFactory(DjangoModelFactory):
    class Meta:
        model = m.Form

    name = f.Sequence(lambda n: f"Формат №{n}")


class SpeakerFactory(DjangoModelFactory):
    class Meta:
        model = m.Speaker

    name = f.Sequence(lambda n: f"Спикер №{n}")


class ThemeFactory(DjangoModelFactory):
    class Meta:
        model = m.Theme

    name = f.Sequence(lambda n: f"Тема №{n}")


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


class Gallery_imageFactory(DjangoModelFactory):
    class Meta:
        model = m.Gallery_image

    image = f.django.ImageField()


class EventFactory(DjangoModelFactory):
    class Meta:
        model = m.Event

    name = f.Sequence(lambda n: f"Ивент №{n}")
    registration_open = f.LazyAttribute(lambda _self: _self.date >= dt.now())

    org = f.SubFactory(UserFactory)
    town = f.SubFactory(TownFactory)
    head_image = f.SubFactory(Gallery_imageFactory)
    form = f.SubFactory(FormFactory)

    date = f.Faker("date_time_this_year", after_now=True)
    video = f.Faker("url")
    description = f.Faker("text")
    address = f.Faker("address")

    @f.post_generation
    def gallery_images(self, create, extracted, **kwargs):
        if create and extracted:
            self.gallery_images.add(*extracted)

    @f.post_generation
    def speakers(self, create, extracted, **kwargs):
        if create and extracted:
            self.speakers.add(*extracted)

    @f.post_generation
    def stack(self, create, extracted, **kwargs):
        if create and extracted:
            self.stack.add(*extracted)

    @f.post_generation
    def specializations(self, create, extracted, **kwargs):
        if create and extracted:
            self.specializations.add(*extracted)


class Program_partFactory(DjangoModelFactory):
    class Meta:
        model = m.Program_part

    name = f.Sequence(lambda n: f"Часть программы №{n}")
    event = f.SubFactory(EventFactory)
    time = f.Faker("time_object")


class ParticipantEventFactory(DjangoModelFactory):
    class Meta:
        model = m.ParticipantEvent

    participant = f.SubFactory(UserFactory)
    event = f.SubFactory(EventFactory)
    participate_online = f.Iterator((True, False))
    agreement_events = True
    agreement_vacancies = True
