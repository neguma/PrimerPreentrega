from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'PreentregaApp/index.html', {})

def guitarras(request):
    return render(request, 'PreentregaApp/guitarras.html', {})

def cuerdas(request):
    return render(request, 'PreentregaApp/cuerdas.html', {})

def mastil(request):
    return render(request, 'PreentregaApp/mastil.html', {})