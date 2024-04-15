from rest_framework import mixins, viewsets


class ListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class ReadPatchViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    pass
