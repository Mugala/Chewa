from django import forms
from .models import Language,Profile,Level,Lesson,Content,Answers,Question


class ProfileDetails (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email',]


class LessonDetails (forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['image']
        widgets = {
            'answers': forms.RadioSelect(),
        }


class LanguageDetails (forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', ]

class AnswersDetails (forms.ModelForm):
    class Meta:

        model = Answers
        fields =['answer','image']

class QuestionDetails (forms.ModelForm):
    class Meta:

        model = Question
        fields =['question']
