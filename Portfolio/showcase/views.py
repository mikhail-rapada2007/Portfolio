from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import Inquiry, Project, PersonalInfo, Testimony, TechStack 
from .forms import ProjectForm, TestimonyForm, TechStackForm, PersonalInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not an admin.'})

    return render(request, 'admin_login.html')

def home(request):
    project_count = Project.objects.count()
    context = {
        'project_count': project_count,
    }
    return render(request, 'home.html', context)

def tutoring(request):
    return render(request, 'tutoring.html')

def project_list(request):
    my_projects = Project.objects.all()
    context = {
        'projects': my_projects,
    }
    return render(request, 'projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
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

@login_required(login_url='admin_login')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = Project(
                project_name=form.cleaned_data['project_name'],
                description=form.cleaned_data['description'],
                link=form.cleaned_data['link'],
            )
            new_project.save()
            new_project.tech_stack.set(form.cleaned_data['tech_stack'])
            return redirect('dashboard')
    else:
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'add_project.html', context)


def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            new_testimony = Testimony(
                full_name=form.cleaned_data['full_name'],
                content=form.cleaned_data['content'],
            )
            new_testimony.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    context = {
        'form': form,
    }
    return render(request, 'add_testimony.html', context)


class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimony_list.html'
    context_object_name = 'testimonies'


def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    context = {
        'testimony': testimony,
    }
    return render(request, 'testimony_detail.html', context)


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        contact_number = request.POST.get('contact_number', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        message = request.POST.get('message', '').strip()

        if not all([first_name, last_name, contact_number, email, address, message]):
            return render(request, 'contact.html', {'error': 'All fields are required.'})

        new_inquiry = Inquiry(
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email=email,
            address=address,
            message=message,
        )
        new_inquiry.save()
        return redirect('home')

    return render(request, 'contact.html')

def admin_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='admin_login')
def add_tech_stack(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            new_tech = TechStack(name=form.cleaned_data['name'])
            new_tech.save()
            return redirect('dashboard')
    else:
        form = TechStackForm()
    context = {
        'form': form,
    }
    return render(request, 'add_tech_stack.html', context)

@login_required(login_url='admin_login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='admin_login')
def dashboard_projects(request):
    projects = Project.objects.all()
    return render(request, 'dashboard_projects.html', {'projects': projects})

@login_required(login_url='admin_login')
def dashboard_tech_stacks(request):
    tech_stacks = TechStack.objects.all()
    return render(request, 'dashboard_tech_stacks.html', {'tech_stacks': tech_stacks})

@login_required(login_url='admin_login')
def dashboard_about_me(request):
    info = PersonalInfo.objects.first()

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            if info is None:
                info = PersonalInfo()
            info.first_name = form.cleaned_data['first_name']
            info.middle_name = form.cleaned_data['middle_name']
            info.last_name = form.cleaned_data['last_name']
            info.summary = form.cleaned_data['summary']
            info.contact_number = form.cleaned_data['contact_number']
            info.email = form.cleaned_data['email']
            info.address = form.cleaned_data['address']
            info.save()
            return redirect('dashboard_about_me')
    else:
        if info:
            form = PersonalInfoForm(initial={
                'first_name': info.first_name,
                'middle_name': info.middle_name,
                'last_name': info.last_name,
                'summary': info.summary,
                'contact_number': info.contact_number,
                'email': info.email,
                'address': info.address,
            })
        else:
            form = PersonalInfoForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard_about_me.html', context)