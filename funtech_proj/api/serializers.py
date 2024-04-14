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
ParticipantEventSerializer = serializer_class_maker(em.ParticipantEvent)
Gallery_imageSerializer = serializer_class_maker(em.Gallery_image)
# EventSerializer = serializer_class_maker(em.Event)
UserSerializer = serializer_class_maker(User)


class EventSerializer(ModelSerializer):
    town = TownSerializer()
    form = FormSerializer()
    # speakers = SpeakerSerializer(many=True)
    # speakers = SpeakerSerializer(many=True, source="speakers_events")
    # gallery_images = Gallery_imageSerializer()
    # image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = em.Event
        # fields = "__all__"
        exclude = ("created", "org", "specializations", "stack", "participants")
