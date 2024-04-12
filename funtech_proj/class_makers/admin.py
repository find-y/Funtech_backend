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
    return _Admin


def inline_maker(model_: Model, m2m_field_name: str) -> admin.TabularInline:
    class _Inline(admin.TabularInline):
        model = getattr(model_, m2m_field_name).through

    return _Inline
