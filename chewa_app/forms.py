from django import forms
from .models import Language,Profile,Level,Lesson,Content


class ProfileDetails (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email',]


class LessonDetails (forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['question', 'answer', 'image','level','language', ]
       


    
class LanguageDetails (forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', ]

