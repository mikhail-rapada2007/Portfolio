from django.shortcuts import render
from .models import Project, PersonalInfo

def home(request):
    return render(request, 'home.html')

def tutoring(request):
    return render(request, 'tutoring.html')

def project_list(request):
    my_projects = Project.objects.all()
    context = {
        'projects': my_projects,
    }
    return render(request, 'projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

def about_me(request):
    info = PersonalInfo.objects.first()
    context = {
        'info': info,
    }
    return render(request, 'about_me.html', context)