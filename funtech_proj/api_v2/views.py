from datetime import date

from api_v2 import serializers as s
from api_v2.viewsets import ListViewSet
from class_makers.api import viewset_class_maker as vscm
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from events import models as em
from events.tasks import background_task
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from shared import models as sm


class TownViewSet(ListViewSet):
    serializer_class = s.TownSerializer
    queryset = sm.Town.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("^name",)


class GenericNameTemplateViewSet(ListViewSet):
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ("name",)
    ordering = ("name",)

    def get_queryset(self):
        background_task.delay()
        return self.serializer_class.Meta.model.objects.all()


class SpecializationViewSet(GenericNameTemplateViewSet):
    serializer_class = s.SpecializationSerializer
    filterset_fields = ("theme",)


class StackViewSet(GenericNameTemplateViewSet):
    serializer_class = s.StackSerializer
    filterset_fields = ("specialization",)


class GenericEventsViewsSet(ListViewSet):
    serializer_class = s.EventSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("town",)
    ordering_fields = ("date",)
    ordering = ("date",)


class ClosestEventsViewsSet(GenericEventsViewsSet):
    queryset = em.Event.objects.exclude(registration_open__exact=False)


EventShortViewSet = vscm(em.Event, s.EventShortSerializer)


class ParticipantEventViewSet(ModelViewSet):
    queryset = em.ParticipantEvent.objects.all()
    serializer_class = s.ParticipantEventSerializer
    # pagination_class = None
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class EventViewSet(ModelViewSet):
    querqueryset = em.Event.objects.filter(date__gte=date.today())
    serializer_class = s.EventSerializer

    @action(
        detail=True,
        methods=["POST", "DELETE"],
        # permission_classes=(IsAuthenticated,),
    )
    def favorite(self, request, pk):
        user = request.user
        data = {"user": user.id, "event_id": pk}
        serializer = s.ParticipantEventSerializer(
            data=data, context={"request": request}
        )
        if request.method == "POST":
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        get_object_or_404(
            em.ParticipantEvent,
            participant=user,
            event=get_object_or_404(em.Event, id=pk),
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
