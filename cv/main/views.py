from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def projects(request):
    return render(request, 'main/projects.html')

def education(request):
    return render(request, 'main/education.html')