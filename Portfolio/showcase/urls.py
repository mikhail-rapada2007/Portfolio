from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutoring/', views.tutoring, name='tutoring'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.about_me, name='about_me'),
    path('projects/add/', views.add_project, name='add_project'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
]