import pytest
from django.conf import settings
from rest_framework.test import APIClient
from shared.models import Specialization, Stack, Theme, Town


def test_anon_client_fixture(anon_client: APIClient) -> None:
    assert isinstance(anon_client, APIClient)


@pytest.mark.parametrize("model", (Town, Stack, Specialization, Theme))
def test_load_data(model):
    assert model.objects.count() == settings.PRELOAD_DATA_BATCH_SIZE
