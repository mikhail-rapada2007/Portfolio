from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutoring/', views.tutoring, name='tutoring'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.about_me, name='about_me'),
]