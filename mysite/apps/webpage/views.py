from django.shortcuts import render

from .models import MyProjects

def under_construction(request):
    return render(request, 'under_construction.html')


def index(request):
    projects = MyProjects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'webpage/index.html', context)