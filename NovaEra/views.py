from django.shortcuts import render

from artigos.models import artigos

# def home_page(request):
#     return render(request, 'pages/home.html')


def informacion(request):
    return render(request, 'pages/informacion.html')