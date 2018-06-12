from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Language,Lesson,Level,Content,Profile,Score,Answers
from .forms import ProfileDetails,LanguageDetails,LessonDetails,AnswersDetails
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import LessonSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


def home_page(request):

    return render(request, 'home.html')

def swahili_page(request):

    return render(request, 'languages/swahili.html')

def swahili_beginning(request):

    return render(request, 'beginner/swahili.html')

def swahili_test1(request):

    return render(request, 'test1/swahili.html')


def luo_page(request):

    return render(request, 'languages/luo.html')

def luo_beginning(request):

    return render(request, 'beginner/luo.html')

def luo_test1(request):
    question= Answers.objects.all()
    single_lesson = Lesson.objects.filter(language_id=3).all()
    
    one_lesson= single_lesson.filter(content__category='Family')
    one= one_lesson.order_by('?')[:1]
    print(one)
    # print(single_lesson)
    # print(one_lesson)

    if request.method == 'POST':
        form= LessonDetails(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.save()
    else:
        form = AnswersDetails()


    return render(request, 'test1/luo.html',{"question":question,"single_lesson":single_lesson,"form":form,"one_lesson":one_lesson,"one":one})


'''
    if 'answer' in request.GET and request.GET["answer"]:
        single_category = request.GET.get("username")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request,'gram/search.html',{"message":message, "username":searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gram/search.html',{"message":message})

'''


def kikuyu_page(request):

    return render(request, 'languages/kikuyu.html')

def kikuyu_beginning(request):

    return render(request, 'beginner/kikuyu.html')

def kikuyu_test1(request):

    return render(request, 'test1/kikuyu.html')

def KSL_page(request):

    return render(request, 'languages/KSL.html')

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
    photo=get_object_or_404(Photos, id=id)
    if current_user in photo.likes.all():
        photo.likes.add(current_user)
        photo.likes.remove(current_user)
    else:
        photo.likes.add(current_user)

    return redirect('/')

class LessonList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_lessons = Lesson.objects.all()
        serializers= LessonSerializer(all_lessons, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers= LessonSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonDescription(APIView):
    permission_classes=(IsAdminOrReadOnly,)
    def get_lesson(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        lesson=self.get_lesson(pk)
        serializers= LessonSerializer(lesson)
        return Response(serializers.data)
    def put(self, request, pk, format=None):
        lesson=self.get_lesson(pk)
        serializers=LessonSerializer(lesson, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        lesson=self.get_lesson(pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
