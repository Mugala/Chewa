from rest_framework import serializers
from .models import Language,Profile,Level,Lesson,Content

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=('id','question', 'answer', 'image','level','language') 