from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from forms import QuestionsForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Все тесты", 'url_name': 'all_tests'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    group_test = Test_group.objects.all()

    context = {
        'group_test': group_test,
        'menu': menu,
        'title': 'Главная страница',
        'tests_selected': 0,
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


def show_tests(request):
    if request.method == 'POST':
        pass
    else:
        form = QuestionsForm()
    return render(request, 'testsite/show_test.html', {'form': form})

# def show_questions(request, questions_id):
#     questions = Question.objects.filter(test_title_id=questions_id)
#     one_question = Question.objects.get(pk=id)
