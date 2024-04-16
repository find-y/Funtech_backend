from typing import Any, TypeAlias

from django.urls import reverse

Dict: TypeAlias = dict[str, Any]
ResponseJson: TypeAlias = Dict | list[Dict]


def contains(item, *words) -> bool:
    for word in words:
        if item.__contains__(word):
            return True
    return False


def get_urls(url_patterns):
    def get_name(item):
        return vars(item).get("name")

    routes = {
        reverse(get_name(item), args=["1"])
        if contains(get_name(item), "detail", "favorite")
        else reverse(get_name(item))
        for item in vars(url_patterns[0]).get("urlconf_name")
    }
    routes.remove("/")
    return routes


def __check(response_json: Dict):
    assert isinstance(response_json, dict), type(response_json)
    assert response_json.get("id")


def check(response_json: ResponseJson) -> bool:
    if isinstance(response_json, dict):
        response_json = [response_json]
    for each in response_json:
        __check(each)
    return True
