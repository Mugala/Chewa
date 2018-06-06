from django.shortcuts import render,redirect
from .models import Language, Content, Profile, Level, Lessons
from .forms import ProfileForm
# Create your views here.

def home_page(request):

    return render(request, 'home.html')


def create_profile(request):
    title="create Profile"
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.save()
            return redirect('createprofile')
    else:
        form=ProfileForm()
    return render(request, 'forms/profile.html', {"title":title, "form":form})