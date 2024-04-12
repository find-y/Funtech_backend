from typing import Any

from django.db.models import Model


def set_extra_fields(
    model_: Model,
    extra_fields: tuple[tuple[str, Any], ...] | None = None,
) -> None:
    if extra_fields is not None:
        for field_name, field_value in extra_fields:
            setattr(model_, field_name, field_value)
