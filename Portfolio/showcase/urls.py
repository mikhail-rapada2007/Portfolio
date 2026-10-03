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
    path('contact/', views.contact, name='contact'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/projects/', views.dashboard_projects, name='dashboard_projects'),
    path('dashboard/tech-stacks/', views.dashboard_tech_stacks, name='dashboard_tech_stacks'),
    path('dashboard/add-projects/', views.add_project, name='add_project'),
    path('dashboard/add-tech-stacks/', views.add_tech_stack, name='add_tech_stack'),
    path('dashboard/about-me/', views.dashboard_about_me, name='dashboard_about_me'),
]