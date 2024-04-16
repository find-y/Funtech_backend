import pytest
from data.load_data import load_db
from rest_framework.test import APIClient


@pytest.fixture
def anon_client() -> APIClient:
    return APIClient()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(autouse=True)
def load_data():
    load_db()


@pytest.fixture(autouse=True)
def mock_celery_delay(monkeypatch):
    def mock_delay(*args, **kwargs):
        pass

    monkeypatch.setattr("api_v2.views.background_task.delay", mock_delay)
