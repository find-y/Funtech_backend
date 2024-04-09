from typing import TypeAlias

from django.contrib import admin

from . import models as m

m2m_model = m.Event
m2m_style: TypeAlias = admin.TabularInline


class Gallery_imageEventInline(m2m_style):
    model = m2m_model.gallery_images.through


class SpeakerEventInline(m2m_style):
    model = m2m_model.speakers.through


class StackEventInline(m2m_style):
    model = m2m_model.stack.through


class SpecializationsEventInline(m2m_style):
    model = m2m_model.specializations.through


m2m_fields = {
    "gallery_images": Gallery_imageEventInline,
    "specializations": SpecializationsEventInline,
    "speakers": SpeakerEventInline,
    "stack": StackEventInline,
}


@admin.register(m.Event)
class EventAdmin(admin.ModelAdmin):
    exclude = tuple(m2m_fields.keys())
    inlines = tuple(m2m_fields.values())


@admin.register(m.Town)
class TownAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Form)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Stack)
class StackAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Gallery_image)
class Galery_imageAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Program_part)
class Program_partAdmin(admin.ModelAdmin):
    pass


@admin.register(m.ParticipantEvent)
class ParticipantEventAdmin(admin.ModelAdmin):
    pass
