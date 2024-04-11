from typing import Any

from django.contrib import admin
from django.db.models import Model

from .utils import set_extra_fields


def admin_class_maker(
    model_: Model, extra_fields: tuple[tuple[str, Any], ...] | None = None
) -> admin.ModelAdmin:
    @admin.register(model_)
    class _Admin(admin.ModelAdmin):
        pass

    set_extra_fields(_Admin, extra_fields)
    """if extra_fields is not None:
        for field_name, field_value in extra_fields:
            setattr(_Admin, field_name, field_value) """

    return _Admin


def inline_maker(
    model_: Model, m2m_field_name: str, m2m_style=admin.TabularInline
) -> admin.TabularInline:
    class _Inline(m2m_style):  # type: ignore
        model = getattr(model_, m2m_field_name).through

    return _Inline
