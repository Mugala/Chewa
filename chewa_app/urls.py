from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


#please do not change the urls.please and thanks*/

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile/', views.profile, name='profile'),
    path('language/', views.language, name='language'),
    path('question/', views.question, name='question'),
    path('answerform/', views.answerform, name='answerform'),
    # path('content/', views.content1, name='category'),
    path('lesson/', views.lesson, name='lesson'),
    path('<language>/level/', views.level, name='level'),
    path('<language>/<level>/lesson', views.content, name='content'),
    path('answer/<point>', views.answer, name='answer'),
    path('api/lessons', views.LessonList.as_view()),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
    path('signup/', views.sign_up, name='sign_up'),
    path('search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
