from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('project/', views.project, name="portfolio"),
    path('skill/', views.skill, name="skill"),
    path('contact/', views.contact, name="contact")
]