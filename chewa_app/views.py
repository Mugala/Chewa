from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Language,Lesson,Level,Content,Profile,Score
from .forms import ProfileDetails,LanguageDetails,LessonDetails
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import LessonSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout
from django.contrib import messages
from social_django.models import UserSocialAuth




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
    question= Lesson.objects.all()
    single_lesson = Lesson.objects.filter(language_id=3).all()
    print(single_lesson)

    if request.method == 'POST':
        form= LessonDetails(request.POST, request.FILES)
        if form.is_valid():
            single_lesson = form.save(commit = False)
            single_lesson.save()
    else:
        form = LessonDetails()

    return render(request, 'test1/luo.html',{"question":question,"single_lesson":single_lesson,"form":form})

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
    answers = get_object_or_404(Lesson, id=id)

    if current_user in answers.likes.all():
        photo.likes.add(current_user)
        photo.likes.remove(current_user)
        print(current_user)
        print("hello")
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

@login_required
def settings(request):
    title="Chewa | Settings"
    user = request.user
    print(user)
    try:
        google_login = user.social_auth.get(provider='google-oauth2')
        
    except UserSocialAuth.DoesNotExist:
        google_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'registration/settings.html', {
        'google_login': google_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    title="Chewa | Password"
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})

def sign_up(request):
    title="Chewa | Sign Up"
    if request.method=='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_page')
    else:form=UserCreationForm()
    return render(request, 'registration/sign_up.html', {"form":form, "title":title})
            

