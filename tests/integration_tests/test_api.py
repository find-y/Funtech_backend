from http import HTTPStatus

import pytest
from api_v1.urls import urlpatterns as v1
from api_v2.urls import urlpatterns as v2
from rest_framework.test import APIClient

from .utils import check, contains, get_urls


@pytest.mark.parametrize(
    "url",
    (
        *get_urls(v1),
        *get_urls(v2),
    ),
)
def test_endpoints_access(anon_client: APIClient, url):
    if contains(url, "list", "detail"):
        response = anon_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.json()
        assert check(response.json())
