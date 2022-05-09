from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить тест', 'Обратная связь', 'Войти']


def index(request):
    posts = test_title.objects.all()
    return render(request, 'testsite/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'testsite/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Категории тестов</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
