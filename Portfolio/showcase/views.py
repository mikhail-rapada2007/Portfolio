from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInfo

def home(request):
    return render(request, 'home.html')

def tutoring(request):
    return render(request, 'tutoring.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def about_me(request):
    info = PersonalInfo.objects.first()
    return render(request, 'about_me.html', {'info': info})