from typing import Any, TypeAlias

from django.urls import reverse

Dict: TypeAlias = dict[str, Any]
ResponseJson: TypeAlias = Dict | list[Dict]


def get_urls(url_patterns):
    routes = {
        reverse(vars(item).get("name"), args=["1"])
        if vars(item).get("name").__contains__("detail")
        else reverse(vars(item).get("name"))
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
