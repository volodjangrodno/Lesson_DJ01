from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # так прописываем если на странице немного информации
    # return HttpResponse("<h1>Это главная страница моего проекта на Django</h1>")
    return render(request, 'main/index.html') # а так прописываем если хотим вызвать целую html- страницу, где много информации

def data(request):
    # так прописываем если на странице немного информации
    # return HttpResponse("<h1>Это страница data моего проекта на Django</h1>")
    return render(request, 'myotherapp/data.html') # а так прописываем если хотим вызвать целую html- страницу, где много информации

def test(request):
    # так прописываем если на странице немного информации
    # return HttpResponse("<h1>Это  страница test моего проекта на Django</h1>")
    return render(request, 'myotherapp/test.html') # а так прописываем если хотим вызвать целую html- страницу, где много информации