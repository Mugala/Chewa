from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
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
from django.urls import resolve
import random
from django.forms.models import model_to_dict


@login_required
def home_page(request):
    current_user=request.user
   
    languages=Language.objects.all()
      
    
    return render(request, 'home.html', {"languages":languages})

@login_required
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

@login_required
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

    return render(request, 'dashboard/language.html', {"language_form":language_form})

@login_required
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

@login_required
def level(request, language):
    language=request.GET.get('language')
    levels=Level.objects.all()
    print(language)
   

    return render(request, 'user/level.html', {"levels":levels, "language":language})

@login_required
def content(request, language, level):
    current_user=request.user
    try:
        current_user=request.user    
        profile=Profile.objects.get(user=current_user)
        print(profile)
        language=request.GET.get('language')
        print(language)
        currentUrl = request.get_full_path()
        lan=currentUrl.split('/')
        
        language=lan[1]
        print(language)
        print(currentUrl)
        level=request.GET.get('level')
        print("here" + level)
        
        contents=Lesson.objects.filter(level__level=level, language__name=language)
        print(contents)
        chosen=random.choice(contents)  
    except:
        return redirect('profile')   
   
    return render(request, 'user/content.html', {"contents":chosen, "profile":profile})
    
@login_required
def answer(request, point):
    current_user=request.user
    point=request.GET.get('point')
    currentUrl = request.get_full_path()
    point=currentUrl.split('/')
    profile=Profile.objects.get(user=current_user)
    profile.total_score+=int(point[-1])
    profile.save()

    print(profile)

    return JsonResponse(model_to_dict(profile), safe=False)


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
            return redirect('profile')
    else:form=UserCreationForm()
    return render(request, 'registration/sign_up.html', {"form":form, "title":title})
            

