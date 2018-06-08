from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Language,Lesson,Level,Content,Profile,Score
from .forms import ProfileDetails,LanguageDetails,LessonDetails

# Create your views here.

def home_page(request):

    return render(request, 'home.html')

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileDetails(request.POST, request.FILES)
        if form.is_valid():
            Profile = form.save(commit=False)
            Profile.user = current_user
            Profile.save()

            return redirect("home_page")
    else:
        form = ProfileDetails()
    
    return render(request, 'dashboard/profile.html', {"form":form})

def language (request):
    current_user = request.user
    if request.method == 'POST':
        form = LanguageDetails(request.POST, request.FILES)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = current_user
            language.save()

            return redirect("home_page")
    else:
        language_form = LanguageDetails()
    
    return render(request, 'dashboard/Language_details.html', {"language_form":language_form})

def lesson (request):
    current_user = request.user
    if request.method == 'POST':
        form = LessonDetails(request.POST, request.FILES)
        if form.is_valid():
            Lesson = form.save(commit=False)
            Lesson.user = current_user
            Lesson.save()

            return redirect("home_page")
    else:
        lesson_form = LessonDetails()
    
    return render(request, 'dashboard/Lesson_details.html', {"lesson_form":lesson_form})