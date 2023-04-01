from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Global/home.html')


def contato(request):
    return HttpResponse('contato 2')


def sobre(request):
    return HttpResponse('sobre 2')
