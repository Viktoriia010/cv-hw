from django.urls import path, include

from . import  views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('education', views.education),
    path('skills', views.skills),
    path('projects', views.projects),
]
