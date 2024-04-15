from api_v2 import views as v
from django.urls import include, path
from rest_framework.routers import DefaultRouter

ROUTES = (
    ("towns", v.TownViewSet),
    ("specializations", v.SpecializationViewSet),
    ("stack", v.StackViewSet),
    ("events", v.EventViewSet),
    ("events_short", v.EventShortViewSet),
    ("events/closest", v.ClosestEventsViewsSet),
)
"""
    ("forms", v.FormViewSet),
    ("themes", v.ThemeViewSet),
    ("speakers", v.SpeakerViewSet),
    ("images", v.GalleryImageViewSet),
    ("program_parts", v.Program_partViewSet),
    ("participants", v.ParticipantEventViewSet),
    ("events/interesting", v.MayBeInterestingViewSet),
    ("events", v.EventViewSet),
    ("users", v.UserViewSet),
"""


router = DefaultRouter()
for url_prefix, view_set in ROUTES:
    router.register(url_prefix, view_set, basename=url_prefix)

urlpatterns = [
    path("/", include(router.urls)),
]
