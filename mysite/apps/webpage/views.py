from django.shortcuts import render


def under_construction(request):
    return render(request, 'under_construction.html')


def index(request):
    return render(request, 'webpage/index.html')