from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('lesson/create/', views.create_lesson, name='create_lesson'),
    path('language/create/', views.add_language, name='add_language'),
    path('content/create/', views.add_content, name='add_content'),
    path('profile/create/', views.create_profile, name='create_profile'),
    
    
]