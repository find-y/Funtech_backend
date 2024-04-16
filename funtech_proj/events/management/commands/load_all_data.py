from data.load_data import load_db
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        load_db(*args, **kwargs)
