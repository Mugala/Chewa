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
    answers = get_object_or_404(Lesson, id=id)

    if current_user in answers.likes.all():
        photo.likes.add(current_user)
        photo.likes.remove(current_user)
        print(current_user)
        print("hello")
    else:
        photo.likes.add(current_user)
        return redirect('/')
    return redirect('/')

#     questions = {
#         "What is Today in Kiswahili?":['a. Jana', 'b. Kesho', 'c. Juzi', 'd. Leo','d'],
#         "What is Afternoon in Kiswahili?":['a. Asubuhi', 'b. Jioni', 'c. Usiku', 'd. Alfajiri', 'd'],
#         "What is hello in Kiswahili?":['a. Habari', 'b. mzuri', 'c. Hapana', 'd. yeye', 'a'],
#         "What is Father in Kiswahili?":['a. Ndugu', 'b. Baba', 'c. Mama', 'd. dada', 'b'],
#         "What is Thank you in Kiswahili?":['a. Ndio', 'b. Mzuri', 'c. Asante', 'd. Kesho', 'c']
#     } 

# score = 0  
# for question_number,question in enumerate(questions,start=1):
#     print ("Question",question_number) 
#     print (question)
#     for options in questions[question][:-1]:
#         print (options)
#     choice = input("Make your choice : ")
#     user_choice = choice.lower()
#     if user_choice == questions[question][-1]:
#         print ("Correct!")
#         score += 1 
#     else: 
#         print ("Wrong!")
# result = "Your total score is " + str(score)

# print(result)
       
    # return redirect('/')
    #     if current_user in photo.likes.all():
    #         photo.likes.add(current_user)
    #         photo.likes.remove(current_user)
    #     else:
    #         photo.likes.add(current_user)
        
    #     return redirect('/')