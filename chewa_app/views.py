from django.shortcuts import render,redirect
from .models import Language, Content, Profile, Easy, Lessons
from .forms import LessonForm, LanguageForm, ContentForm, ProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .serializer import LessonsSerializer
from .permissions import IsAdminOrReadOnly


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

class LessonList(APIView):
    def get(self, request, format=None):
        all_lessons=Lessons.objects.all()
        serializers=LessonsSerializer(all_lessons, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers=LessonsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)
       

def add_language(request):
    title="add languaged"
    form=LanguageForm(request.POST)
    if form.is_valid():
        language=form.save(commit=False)
        language.save()
        return redirect('home_page')
    else:
        form=LanguageForm()
    return render(request, 'forms/language.html', {"title":title, "form":form})

def add_content(request):
    title="Content"
    form=ContentForm(request.POST)
    if form.is_valid():
        content=form.save(commit=False)
        content.save()
        return redirect('home_page')
    else:
        form=ContentForm()
    return render(request, 'forms/content.html', {"title":title, "form":form})
    

def create_profile(request):
    title="create Profile"
    form=ProfileForm(request.POST)
    if form.is_valid():
        profile=form.save(commit=False)
        profile.save()
        return redirect('home_page')
    else:
        form=ProfileForm()
    return render(request, 'forms/profile.html', {"title":title, "form":form})
