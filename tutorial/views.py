from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'name': 'index'})


def tutorial(request):
    return render(request, 'tutorial/tutorial.html', {'name': 'tutorial'})
