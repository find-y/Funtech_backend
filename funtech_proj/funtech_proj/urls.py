from django.contrib import admin
from django.urls import include, path
from drf_spectacular import views as sv

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", sv.SpectacularAPIView.as_view(), name="schema"),
    path("docs/", sv.SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("redoc/", sv.SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/v1", include("api_v1.urls")),
    path("api/v2", include("api_v2.urls")),
]
