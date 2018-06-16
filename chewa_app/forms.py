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

<<<<<<< HEAD
class AnswersDetails (forms.ModelForm):
    class Meta:

        model = Answers
        fields =['answer','image']

=======
>>>>>>> 9e4e68da1c3407c9783de5c11aa041279c074d85
class EditProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['name', 'email']
<<<<<<< HEAD
        
class QuestionDetails (forms.ModelForm):
    class Meta:

        model = Question
        fields =['question']
=======
>>>>>>> 9e4e68da1c3407c9783de5c11aa041279c074d85
