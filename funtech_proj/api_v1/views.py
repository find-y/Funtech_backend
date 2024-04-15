from api_v1 import serializers as s
from api_v1.viewsets import ReadPatchViewSet
from class_makers.api import viewset_class_maker as vscm
from events import models as em
from shared import models as sm
from users.models import User

TownViewSet = vscm(sm.Town, s.TownSerializer)
FormViewSet = vscm(sm.Form, s.FormSerializer)
ThemeViewSet = vscm(sm.Theme, s.ThemeSerializer)
StackViewSet = vscm(sm.Stack, s.StackSerializer)
SpecializationViewSet = vscm(sm.Specialization, s.SpecializationSerializer)

GalleryImageViewSet = vscm(em.Gallery_image, s.Gallery_imageSerializer)
SpeakerViewSet = vscm(em.Speaker, s.SpeakerSerializer)
Program_partViewSet = vscm(em.Program_part, s.Program_partSerializer)
ParticipantEventViewSet = vscm(em.ParticipantEvent, s.ParticipantEventSerializer)

EventViewSet = vscm(em.Event, s.EventSerializer, ReadPatchViewSet)
EventShortViewSet = vscm(em.Event, s.EventShortSerializer)
UserViewSet = vscm(User, s.UserSerializer, ReadPatchViewSet)
