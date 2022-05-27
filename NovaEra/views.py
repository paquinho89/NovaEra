from django.shortcuts import render

from artigos.models import artigos

# def home_page(request):
#     return render(request, 'pages/home.html')


def information_view(request):
  return render (request, 'informacion.html')