# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import (Event, Town, Form, SpeakerEvent, Galery_image)
# from .utils import Base64ImageField


class TownSerializer(ModelSerializer):

    class Meta:
        model = Town
        fields = "__all__"


class FormSerializer(ModelSerializer):

    class Meta:
        model = Form
        fields = "__all__"


class SpeakerEventSerializer(ModelSerializer):

    class Meta:
        model = SpeakerEvent
        fields = "__all__"


class Galery_imageSerializer(ModelSerializer):

    class Meta:
        model = Galery_image
        fields = "__all__"


class EventSerializer(ModelSerializer):
    town = TownSerializer()
    form = FormSerializer()
    speakers = SpeakerEventSerializer(many=True, source="speakers_events")
    # galery_images = Galery_imageSerializer()
    # image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Event
        # fields = "__all__"
        exclude = ('created', 'org', 'specialization', 'stack', 'participants')
