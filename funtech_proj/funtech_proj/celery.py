import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "funtech_proj.settings")

app = Celery("funtech_proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
