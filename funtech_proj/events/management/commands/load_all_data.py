from data import factories as f
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory

from funtech_proj.settings import PRELOAD_DATA_BATCH_SIZE as SIZE

"""from data.factories import (
    Galery_imageFactory,
    Program_partFactory,
    SpeakerFactory,
    TagFactory,
    TownFactory,
)"""
# from utils import info


# @info
def create_batch(_class: DjangoModelFactory) -> None:
    _class.create_batch(SIZE)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _class in (
            f.Galery_imageFactory,
            f.Program_partFactory,
            f.SpeakerFactory,
            f.TagFactory,
            f.TownFactory,
            f.UserFactory,
        ):
            create_batch(_class)
