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


def inline_m2m_maker(m2m_model: Model, m2m_field_name: str) -> admin.TabularInline:
    class M2M_Inline(admin.TabularInline):
        model = getattr(m2m_model, m2m_field_name).through

    return M2M_Inline


def inline_fk_maker(fk_model: Model) -> admin.TabularInline:
    class FK_Inline(admin.TabularInline):
        model = fk_model

    return FK_Inline
