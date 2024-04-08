import logging
import random

from data import factories as f
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory

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
    items: list[f.DjangoModelFactory], size: int = 3
) -> list[f.DjangoModelFactory]:
    return (
        sorted(random.choices(items, k=size), key=lambda item: item.id)
        if size < len(items)
        else items
    )


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        get_or_create_batch(f.TownFactory)
        participants = get_or_create_batch(f.UserFactory)
        galery_images = get_or_create_batch(f.Galery_imageFactory)
        program_parts = get_or_create_batch(f.Program_partFactory)
        speakers = get_or_create_batch(f.SpeakerFactory)
        tags = get_or_create_batch(f.TagFactory)
        get_or_create_batch(
            f.EventFactory,
            galery_images=get_random(galery_images),
            participants=get_random(participants),
            program_parts=get_random(program_parts),
            speakers=get_random(speakers),
            tags=get_random(tags),
        )
