from django.urls import path
from main import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('about_me/', views.AboutMeView.as_view()),
    path('skill/', views.SkillView.as_view()),
]