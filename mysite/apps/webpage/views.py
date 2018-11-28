from django.shortcuts import render


def index(request):
    return render(request, 'under_construction.html')