from class_makers.admin import admin_class_maker, inline_maker
from events import models as m

PARTICIPANTS = "participants"
SPECIALIZATIONS = "specializations"
STACKS = "stacks"

m2m_model = m.Event
m2m_fields = {
    PARTICIPANTS: inline_maker(m2m_model, PARTICIPANTS),
    SPECIALIZATIONS: inline_maker(m2m_model, SPECIALIZATIONS),
    STACKS: inline_maker(m2m_model, STACKS),
}
EventAdmin = admin_class_maker(
    m2m_model,
    extra_fields=(
        ("exclude", tuple(m2m_fields.keys())),
        ("inlines", tuple(m2m_fields.values())),
    ),
)

SpeakerAdmin = admin_class_maker(m.Speaker)
Program_partAdmin = admin_class_maker(m.Program_part)
ParticipantEventAdmin = admin_class_maker(m.ParticipantEvent)
Galery_imageAdmin = admin_class_maker(m.Gallery_image)
