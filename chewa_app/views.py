from django.shortcuts import render,redirect, get_object_or_404
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

def user_score(request, id):
    current_user=request.user
    current_user=request.user
    answers = get_object_or_404(Lesson, id=id)

    questions = {
        "How tall is the Eiffel Tower?":['a. 350m', 'b. 342m', 'c. 324m', 'd. 1000ft','a'],
        "How loud is a sonic boom?":['a. 160dB', 'b. 175dB', 'c. 157dB', 'd. 213dB', 'd']
    } 

    score = 0  
    for question_number,question in enumerate(questions):
        print ("Question",question_number+1) 
        print (question)
        for options in questions[question][:-1]:
            print (options)
        user_choice = input("Make your choice : ")
        if user_choice == questions[question][-1]:
            print ("Correct!")
            score += 1 
        else: 
            print ("Wrong!")

    print(score) 
       
    return redirect('/')
    if current_user in photo.likes.all():
        photo.likes.add(current_user)
        photo.likes.remove(current_user)
    else:
        photo.likes.add(current_user)
       
    return redirect('/')