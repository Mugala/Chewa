from django import forms
from .models import Language, Content, Profile, Easy, Lessons

class LessonForm(forms.ModelForm):
    class Meta:
        model=Lessons
        fields=('Question', 'Answer', 'Language', 'category','Level')

class LevelForm(forms.ModelForm):
    class Meta:
        model=Easy
        fields=('easy_or_hard',)
        widgets = {
            'easy_or_hard': forms.RadioSelect
        }
