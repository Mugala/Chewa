from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


#please do not change the urls.please and thanks*/

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home_page, name='home_page'),
    path('profile/', views.profile, name='profile'),
    path('translate/', views.translator, name='translate'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/view', views.view_profile, name='view_profile'),
    path('language/', views.language, name='language'),
    # path('content/', views.content1, name='category'),
    path('swa-begin', views.swahili_beginning, name='swa-begin'),
    path('lesson/', views.lesson, name='lesson'),
    path('<language>/level/', views.level, name='level'),
    path('<language>/<level>/lesson', views.content, name='content'),
    path('answer/<point>', views.answer, name='answer'),
    path('api/lessons', views.LessonList.as_view()),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
    path('signup/', views.sign_up, name='sign_up'),
    path('search/', views.search_results, name='search_results'),
    path('next/',views.hear_it, name="hear_it"),
    path('swa_family/',views.swa_family, name="swa_family"),
    path('swa_family/next/',views.swa_family_audio, name="swa_family_audio"),
    path('kikuyu_family/',views.kikuyu_family, name="kikuyu_family"),
    path('kikuyu-begin', views.kikuyu_beginning, name="kikuyu-begin"),
    path('kikuyu/next/',views.kikuyu_hear_it, name="kikuyu_hear_it"),
    path('kikuyu_family/next/',views.kikuyu_family_audio, name="kikuyu_family_audio"),

    path('luo_family/',views.luo_family, name="luo_family"),
    path('luo-begin', views.luo_beginning, name="luo-begin"),
    path('luo/next/',views.luo_hear_it, name="luo_hear_it"),
    path('luo_family/next/',views.luo_family_audio, name="luo_family_audio"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
