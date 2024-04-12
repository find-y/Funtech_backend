import logging
import random

from data import events_factories as ef
from data import shared_factories as sf
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory
from users.models import User

from funtech_proj.settings import PRELOAD_DATA_BATCH_SIZE as SIZE

logging.basicConfig(level=logging.INFO)


def get_or_create_batch(_class: DjangoModelFactory, **kwargs) -> list:
    if _class._meta.model.objects.exists():
        logging.info(f"{_class.__name__} data already exists... exiting.")
        return _class._meta.model.objects.all()
    logging.info(f"=Loading {_class.__name__} data")
    created = _class.create_batch(SIZE, **kwargs)
    logging.info(f"=== {created}")
    return created


def get_random(
    items: list[DjangoModelFactory], size: int = 3
) -> list[DjangoModelFactory]:
    return (
        sorted(random.choices(items, k=size), key=lambda item: item.id)
        if size < len(items)
        else items
    )


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        events = get_or_create_batch(
            ef.EventFactory,
            stacks=get_random(get_or_create_batch(sf.StackFactory)),
            specializations=get_random(get_or_create_batch(sf.SpecializationFactory)),
        )
        users = reversed(User.objects.all())
        for event in events:
            ef.Gallery_imageFactory(event=event)
            ef.Program_partFactory(event=event)
            ef.SpeakerFactory(event=event)

        for event, user in zip(events, users):
            ef.ParticipantEventFactory(participant=user, event=event)
