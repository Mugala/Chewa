from django.urls import path
from . import views 
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lesson/create/', views.create_lesson, name='create_lesson'),
    path('language/create/', views.add_language, name='add_language'),
    path('content/create/', views.add_content, name='add_content'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('api/lessons', views.LessonList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
    
]