from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # так прописываем если на странице не много информации
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'main/index.html', {'caption':'Хомяк-Комбо на Django'}) # а так прописываем если хотим вызвать целую html- страницу, где много информации

def new(request):
    # так прописываем если на странице немного информации
    # return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/new.html') # а так прописываем если хотим вызвать целую html- страницу, где много информации
