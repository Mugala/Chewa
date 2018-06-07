from django.contrib import admin
from .models import Language, Content, Profile, Easy, Lessons


admin.site.register(Language)
admin.site.register(Content)
admin.site.register(Profile)
admin.site.register(Easy)
admin.site.register(Lessons)