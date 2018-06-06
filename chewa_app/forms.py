from django import forms
from .models import Language,Profile,Level,Lessons,Content


class ProfileDetails (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email',]


class LessonDetails (forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['question', 'answer', 'image', ]
        widgets = {
            'Language': forms.CheckboxSelectMultiple(),
        }
        


class LanguageDetails (forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', ]

