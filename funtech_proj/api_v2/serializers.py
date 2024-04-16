from class_makers.api import serializer_class_maker
from events import models as em

# from rest_framework import relations, serializers
from rest_framework.serializers import ModelSerializer
from shared import models as sm
from users.models import User

TownSerializer = serializer_class_maker(sm.Town)
FormSerializer = serializer_class_maker(sm.Form)
ThemeSerializer = serializer_class_maker(sm.Theme)
StackSerializer = serializer_class_maker(sm.Stack)
SpecializationSerializer = serializer_class_maker(sm.Specialization)

SpeakerSerializer = serializer_class_maker(em.Speaker)
Program_partSerializer = serializer_class_maker(em.Program_part)
# ParticipantEventSerializer = serializer_class_maker(em.ParticipantEvent)
Gallery_imageSerializer = serializer_class_maker(em.Gallery_image)
# EventSerializer = serializer_class_maker(em.Event)
UserSerializer = serializer_class_maker(User)


class EventSerializer(ModelSerializer):
    town = TownSerializer()
    form = FormSerializer()
    gallery_images = Gallery_imageSerializer(many=True, read_only=True)
    speakers = SpeakerSerializer(many=True, read_only=True)
    program_parts = Program_partSerializer(many=True, read_only=True)
    specializations = SpecializationSerializer(many=True, read_only=True)
    stacks = StackSerializer(many=True, read_only=True)
    # image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = em.Event
        fields = [
            "id",
            "specializations",
            "stacks",
            "name",
            "date",
            "town",
            "registration_open",
            "form",
            "head_image",
            "description",
            "gallery_images",
            "speakers",
            "program_parts",
            "address",
            "video_link",
        ]


class EventShortSerializer(EventSerializer):
    class Meta(EventSerializer.Meta):
        fields = [
            "id",
            "head_image",
            "town",
            "address",
            "date",
            "name",
            "description",
            "registration_open",
            "specializations",
            "stacks",
        ]


class ParticipantEventSerializer(ModelSerializer):
    class Meta:
        model = em.ParticipantEvent
        fields = "__all__"
