from typing import TypeAlias

from django.contrib import admin

from . import models as m

m2m_model = m.Event
m2m_style: TypeAlias = admin.TabularInline


class Galery_imageEventInline(m2m_style):
    model = m2m_model.galery_images.through


class SpeakerEventInline(m2m_style):
    model = m2m_model.speakers.through


class Program_partEventInline(m2m_style):
    model = m2m_model.program_parts.through


class ParticipantEventInline(m2m_style):
    model = m2m_model.participants.through


class TagEventInline(m2m_style):
    model = m2m_model.tags.through


m2m_fields = {
    "galery_images": Galery_imageEventInline,
    "participants": ParticipantEventInline,
    "program_parts": Program_partEventInline,
    "speakers": SpeakerEventInline,
    "tags": TagEventInline,
}


@admin.register(m.Event)
class EventAdmin(admin.ModelAdmin):
    exclude = tuple(m2m_fields.keys())
    inlines = tuple(m2m_fields.values())


@admin.register(m.Town)
class TownAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Galery_image)
class Galery_imageAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Program_part)
class Program_partAdmin(admin.ModelAdmin):
    pass


@admin.register(m.Tag)
class TagAdmin(admin.ModelAdmin):
    pass
