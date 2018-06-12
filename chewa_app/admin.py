from django.contrib import admin
from .models import Language,Profile,Level,Lesson,Content,Answers

# Register your models here.


class LessonsAdmin(admin.ModelAdmin):
    filter_horizontal = ('Language',)

admin.site.register(Answers)
admin.site.register(Language)
admin.site.register(Profile)
admin.site.register(Level)
admin.site.register(Lesson)
admin.site.register(Content)
