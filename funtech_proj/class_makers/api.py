from django.db.models import Model
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer


def serializer_class_maker(
    model_: Model,
    fields_: tuple[str] | str = "__all__",
) -> ModelSerializer:
    class _Serializer(ModelSerializer):
        class Meta:
            model = model_
            fields = fields_

    return _Serializer


def viewset_class_maker(
    model_: Model,
    serializer__class_: ModelSerializer,
    viewset=viewsets.ReadOnlyModelViewSet,
) -> viewsets.ViewSet:
    class _ViewSet(viewset):  # type: ignore
        queryset = model_.objects.all()
        serializer_class = serializer__class_
        http_method_names = ["get", "patch"]

    return _ViewSet
