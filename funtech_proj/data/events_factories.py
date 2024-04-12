from datetime import datetime as dt

from events.models import Event, Gallery_image, ParticipantEvent, Program_part, Speaker
from factory import (
    Faker,
    Iterator,
    LazyAttribute,
    Sequence,
    SubFactory,
    post_generation,
)
from factory.django import DjangoModelFactory, ImageField

from .shared_factories import FormFactory, TownFactory
from .user_factory import UserFactory


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    registration_open = LazyAttribute(lambda _self: _self.date >= dt.now().date())

    org = SubFactory(UserFactory)
    town = SubFactory(TownFactory)
    form = SubFactory(FormFactory)

    date = Faker("date_this_year", after_today=True)
    head_image = ImageField()
    name = Sequence(lambda n: f"Ивент №{n}")
    description = Faker("text")
    address = Faker("address")
    video_link = Faker("url")

    @post_generation
    def specializations(self, create, extracted, **kwargs):
        if create and extracted:
            self.specializations.add(*extracted)

    @post_generation
    def stacks(self, create, extracted, **kwargs):
        if create and extracted:
            self.stacks.add(*extracted)


class Gallery_imageFactory(DjangoModelFactory):
    class Meta:
        model = Gallery_image

    event = None
    image = ImageField()


class SpeakerFactory(DjangoModelFactory):
    class Meta:
        model = Speaker

    name = Sequence(lambda n: f"ФИО №{n}")
    event = None
    position = Faker("job")
    photo = ImageField()


class Program_partFactory(DjangoModelFactory):
    class Meta:
        model = Program_part

    name = Sequence(lambda n: f"Часть программы №{n}")
    event = None
    time = Faker("time_object")


class ParticipantEventFactory(DjangoModelFactory):
    class Meta:
        model = ParticipantEvent

    participant = None
    event = None
    participate_online = Iterator((True, False))
    agreement_events = Iterator((True, False))
    agreement_vacancies = Iterator((True, False))
