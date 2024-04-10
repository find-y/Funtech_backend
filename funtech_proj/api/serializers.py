# from rest_framework import serializers
from events.models import Event, Form, Gallery_image, Speaker, Town
from rest_framework.serializers import ModelSerializer

# from .utils import Base64ImageField


class TownSerializer(ModelSerializer):
    class Meta:
        model = Town
        fields = "__all__"


class FormSerializer(ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"


class SpeakerSerializer(ModelSerializer):
    class Meta:
        model = Speaker
        fields = "__all__"


class Gallery_imageSerializer(ModelSerializer):
    class Meta:
        model = Gallery_image
        fields = "__all__"


class EventSerializer(ModelSerializer):
    town = TownSerializer()
    form = FormSerializer()
    # speakers = SpeakerSerializer(many=True)
    # speakers = SpeakerSerializer(many=True, source="speakers_events")
    # gallery_images = Gallery_imageSerializer()
    # image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Event
        # fields = "__all__"
        exclude = ("created", "org", "specialization", "stack", "participants")
