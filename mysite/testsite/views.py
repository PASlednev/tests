from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Все тесты", 'url_name': 'all_tests'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    posts = Test_group.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'testsite/index.html', context=context)


def about(request):
    return render(request, 'testsite/about.html', {'menu': menu, 'title': 'О сайте'})


def all_tests(request):
    return HttpResponse("Все тесты")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_group_test(request, group_test_id):
    return HttpResponse(f"Отображение теста с id = {group_test_id}")
