from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bienvenido(request):
    return render(request, 'bienvenido.html')

def despedida(request):
    return HttpResponse('Adios Mundo desde Django')
