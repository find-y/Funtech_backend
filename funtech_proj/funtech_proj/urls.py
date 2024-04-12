from django.contrib import admin
from django.urls import include, path
from drf_spectacular import views as sv

# from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", sv.SpectacularAPIView.as_view(), name="schema"),
    path("docs/", sv.SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("redoc/", sv.SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/", include("api.urls")),
    # path("api-token-auth/", views.obtain_auth_token),
]
