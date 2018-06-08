from rest_framework import serializers
from .models import Language, Content, Profile, Easy, Lessons

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lessons
        fields=('Question', 'Answer', 'Language', 'category','Easy')