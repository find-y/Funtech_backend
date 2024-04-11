from typing import Any

import factory
from django.db.models import Model
from factory.django import DjangoModelFactory

from .utils import set_extra_fields


def template_name_class_maker(
    model_: Model,
    verbose_name: str,
    extra_fields: tuple[tuple[str, Any], ...] | None = None,
) -> DjangoModelFactory:
    class _Factory(DjangoModelFactory):
        name = factory.Sequence(lambda n: f"{verbose_name} №{n}")

        class Meta:
            model = model_

    set_extra_fields(_Factory, extra_fields)

    return _Factory
