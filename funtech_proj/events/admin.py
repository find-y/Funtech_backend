from django.contrib import admin

from .models import (
    Event,
    Galery_image,
    Galery_imageEvent,
    ParticipantEvent,
    Program_part,
    # Program_partEvent,
    Speaker,
    SpeakerEvent,
    # Tag,
    # TagEvent,
    Specialization,
    Stack,
    Town,
    Form,
    Theme,
    SpecializationEvent,
    StackEvent,
)


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    pass


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(Galery_image)
class Galery_imageAdmin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(Program_part)
class Program_partAdmin(admin.ModelAdmin):
    pass


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    pass


class Galery_imageEventInline(admin.TabularInline):
    model = Galery_imageEvent


class SpeakerEventInline(admin.TabularInline):
    model = SpeakerEvent


# class Program_partEventInline(admin.TabularInline):
#     model = Program_partEvent


class Program_partInline(admin.TabularInline):
    model = Program_part


class ParticipantEventInline(admin.TabularInline):
    model = ParticipantEvent


# class TagEventInline(admin.TabularInline):
#     model = TagEvent


class SpecializationEventInline(admin.TabularInline):
    model = SpecializationEvent


class StackEventInline(admin.TabularInline):
    model = StackEvent


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        Galery_imageEventInline,
        SpeakerEventInline,
        # Program_partEventInline,
        Program_partInline,
        ParticipantEventInline,
        # TagEventInline,
        SpecializationEventInline,
        StackEventInline,
    ]
