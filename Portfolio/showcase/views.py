from django.shortcuts import redirect, render
from .models import Project, PersonalInfo
from .forms import ProjectForm
from .models import Project


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

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = Project(
                project_name=form.cleaned_data['project_name'],
                description=form.cleaned_data['description'],
                tech_stack=form.cleaned_data['tech_stack'],
                link=form.cleaned_data['link'],
            )
            new_project.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'add_project.html', context)