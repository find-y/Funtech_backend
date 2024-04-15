from api_v1 import views as v
from django.urls import include, path
from rest_framework.routers import DefaultRouter

ROUTES = (
    ("towns", v.TownViewSet),
    ("forms", v.FormViewSet),
    ("themes", v.ThemeViewSet),
    ("speakers", v.SpeakerViewSet),
    ("specializations", v.SpecializationViewSet),
    ("stack", v.StackViewSet),
    ("images", v.GalleryImageViewSet),
    ("program_parts", v.Program_partViewSet),
    ("participants", v.ParticipantEventViewSet),
    ("events", v.EventViewSet),
    ("events_short", v.EventShortViewSet),
    ("users", v.UserViewSet),
)

v1_router = DefaultRouter()
for url_prefix, view_set in ROUTES:
    v1_router.register(url_prefix, view_set, basename=url_prefix)

urlpatterns = [
    path("/", include(v1_router.urls)),
]
