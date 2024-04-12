import factory as f
from factory.django import DjangoModelFactory
from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = f.Sequence(lambda n: f"Username_{n}")
    email = f.LazyAttribute(lambda _self: f"{_self.username.lower()}@example.com")
    first_name = f.Faker("first_name")
    last_name = f.Faker("last_name")
    password = f.Faker("password")
    mobilefone = f.Faker("msisdn")
    workplace = f.Sequence(lambda n: f"Место работы №{n}")
    position = f.Faker("job")
    experience = f.Iterator(User.EXPERIENCE_CHOICES)
