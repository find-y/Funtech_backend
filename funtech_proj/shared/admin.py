from class_makers.admin import admin_class_maker
from shared import models as m

TownAdmin = admin_class_maker(m.Town)
FormAdmin = admin_class_maker(m.Form)
ThemeAdmin = admin_class_maker(m.Theme)
SpecializationAdmin = admin_class_maker(m.Specialization)
StackAdmin = admin_class_maker(m.Stack)
