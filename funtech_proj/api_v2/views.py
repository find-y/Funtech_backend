from api_v2 import serializers as s
from api_v2.viewsets import ListViewSet
from django_filters.rest_framework import DjangoFilterBackend
from events import models as em
from events.tasks import background_task
from rest_framework import filters
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


"""
class MayBeInterestingViewSet(GenericEventsViewsSet):

    def get_queryset(self):
        # 1 stacks
        # 2 specializations
        return sm.Specialization.objects.filter(
            town__exact=self.request.user.
            registration_open__exact=True,
        ).order_by("date")
"""
