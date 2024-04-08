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


class Galery_imageFactory(DjangoModelFactory):
    image = f.django.ImageField()

    class Meta:
        model = m.Galery_image


class SpeakerFactory(DjangoModelFactory):
    name = f.Sequence(lambda n: f"Спикер №{n}")

    class Meta:
        model = m.Speaker


class Program_partFactory(DjangoModelFactory):
    name = f.Sequence(lambda n: f"Часть №{n} программы")

    class Meta:
        model = m.Program_part


class TagFactory(DjangoModelFactory):
    name = f.Sequence(lambda n: f"Ключевой навык №{n}")

    class Meta:
        model = m.Tag


class TownFactory(DjangoModelFactory):
    name = f.Sequence(lambda n: f"Город №{n}")

    class Meta:
        model = m.Town


class EventFactory(DjangoModelFactory):
    class Meta:
        model = m.Event

    name = f.Sequence(lambda n: f"Ивент №{n}")
    description = f.Faker("text")
    address = f.Faker("address")
    org = f.SubFactory(UserFactory)
    town = f.SubFactory(TownFactory)
    date = f.Faker("date_time_this_year")
    video = f.Faker("url")
    head_image = f.SubFactory(Galery_imageFactory)
    # f.django.ImageField()
    registration_open = f.LazyAttribute(lambda _self: _self.date >= dt.now())

    @f.post_generation
    def galery_images(self, create, extracted, **kwargs):
        if create and extracted:
            self.galery_images.add(*extracted)

    @f.post_generation
    def participants(self, create, extracted, **kwargs):
        if create and extracted:
            self.participants.add(*extracted)

    @f.post_generation
    def program_parts(self, create, extracted, **kwargs):
        if create and extracted:
            self.program_parts.add(*extracted)

    @f.post_generation
    def speakers(self, create, extracted, **kwargs):
        if create and extracted:
            self.speakers.add(*extracted)

    @f.post_generation
    def tags(self, create, extracted, **kwargs):
        if create and extracted:
            self.tags.add(*extracted)
