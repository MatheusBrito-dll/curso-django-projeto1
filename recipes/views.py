from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Matheus Brito',
    })


def teste(request):
    return render(request, 'recipes/pages/teste.html')
