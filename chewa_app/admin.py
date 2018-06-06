from django.contrib import admin
from .models import Language, Content, Profile, Level, Lessons


admin.site.register(Language)
admin.site.register(Content)
admin.site.register(Profile)
admin.site.register(Level)
admin.site.register(Lessons)