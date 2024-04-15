from class_makers.api import serializer_class_maker
from events import models as em
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
EventSerializer = serializer_class_maker(em.Event)
UserSerializer = serializer_class_maker(User)
