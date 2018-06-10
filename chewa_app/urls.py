from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile', views.profile, name='profile'),
    path('language', views.language, name='language'),
    path('lesson', views.lesson, name='lesson'),
    path('api/lessons', views.LessonList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/lesson/lesson-id/<int:pk>/',
        views.LessonDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)