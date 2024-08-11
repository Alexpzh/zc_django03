from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')
    #return HttpResponse('<h1>Это мой первый проект на Django</h1>')

def new(request):
    return render(request, 'main/new.html')
    #return HttpResponse('<h1>Это новая страница проекта на Django</h1>')

