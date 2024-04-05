import factory
from events.models import Galery_image, Program_part, Speaker, Tag, Town
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"Username_{n}")
    email = factory.LazyAttribute(lambda _self: f"{_self.username.lower()}@example.com")
    password = factory.Faker("password")


class Galery_imageFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Изображение №{n}")
    # upload_to = factory.Sequence(
    # lambda n: f"events/images/galery_images/изображение_{n}.png")

    class Meta:
        model = Galery_image


class SpeakerFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Спикер №{n}")

    class Meta:
        model = Speaker


class Program_partFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Часть №{n} программы")

    class Meta:
        model = Program_part


class TagFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Ключевой навык №{n}")

    class Meta:
        model = Tag


class TownFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Город №{n}")

    class Meta:
        model = Town
