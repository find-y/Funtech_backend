import pytest
from data.load_data import load_db
from rest_framework.test import APIClient


@pytest.fixture
def anon_client() -> APIClient:
    return APIClient()


@pytest.fixture(autouse=True)
def load_data(db):
    load_db()


"""
@pytest.fixture(autouse=True)  #, scope='session')
def del_db_env(monkeypatch) -> None:
    monkeypatch.delenv("DB_ENGINE", raising=False)
"""
