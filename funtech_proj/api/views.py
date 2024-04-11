from api import serializers as s
from api.viewsets import ReadPatchViewSet
from class_makers.api import viewset_class_maker as vscm
from events import models as m
from users.models import User

TownViewSet = vscm(m.Town, s.TownSerializer)
FormViewSet = vscm(m.Form, s.FormSerializer)
ThemeViewSet = vscm(m.Theme, s.ThemeSerializer)
StackViewSet = vscm(m.Stack, s.StackSerializer)
GalleryImageViewSet = vscm(m.Gallery_image, s.Gallery_imageSerializer)
SpeakerViewSet = vscm(m.Speaker, s.SpeakerSerializer)
SpecializationViewSet = vscm(m.Specialization, s.SpecializationSerializer)
Program_partViewSet = vscm(m.Program_part, s.Program_partSerializer)
ParticipantEventViewSet = vscm(m.ParticipantEvent, s.ParticipantEventSerializer)

EventViewSet = vscm(m.Event, s.EventSerializer, ReadPatchViewSet)
UserViewSet = vscm(User, s.UserSerializer, ReadPatchViewSet)
