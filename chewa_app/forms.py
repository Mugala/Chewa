from django import forms
from .models import Language, Content, Profile, Level, Lessons

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Lessons
        fields=('Question', 'Answer', 'Language', 'category','Level')
