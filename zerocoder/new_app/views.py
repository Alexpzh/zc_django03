from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Приложение new_app - главная страница</h1>')

def test(request):
    return HttpResponse('<h1>Приложение new_app - страница Test</h1>')

def data(request):
    return HttpResponse('<h1>Приложение new_app - страница данных (data)</h1>')
