from django.shortcuts import render,redirect
from .models import Language, Content, Profile, Easy, Lessons
from .forms import LessonForm
# Create your views here.

def home_page(request):

    return render(request, 'home.html')


def create_lesson(request):
    title="create Profile"
    current_user=request.user
    if request.method=='POST':
        form=LessonForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.save()
            return redirect('home_page')
    else:
        form=LessonForm()
    return render(request, 'forms/lesson.html', {"title":title, "form":form})