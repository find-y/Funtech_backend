from class_makers.api import serializer_class_maker
from events import models as em
from users.models import User

TownSerializer = serializer_class_maker(em.Town)
FormSerializer = serializer_class_maker(em.Form)
ThemeSerializer = serializer_class_maker(em.Theme)
StackSerializer = serializer_class_maker(em.Stack)
SpeakerSerializer = serializer_class_maker(em.Speaker)
SpecializationSerializer = serializer_class_maker(em.Specialization)
Program_partSerializer = serializer_class_maker(em.Program_part)
ParticipantEventSerializer = serializer_class_maker(em.ParticipantEvent)
Gallery_imageSerializer = serializer_class_maker(em.Gallery_image)
EventSerializer = serializer_class_maker(em.Event)
UserSerializer = serializer_class_maker(User)
