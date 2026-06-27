from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def tutoring(request):
    return render(request, 'tutoring.html')