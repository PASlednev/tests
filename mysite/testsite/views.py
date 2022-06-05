from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Все тесты", 'url_name': 'all_tests'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


# class ShowGroup(ListView):
#     model = Test_group
#     template_name = 'testsite/index.html'
#     context_object_name = 'test'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = [{'title': "О сайте", 'url_name': 'about'},
#                            {'title': "Все тесты", 'url_name': 'all_tests'},
#                            {'title': "Обратная связь", 'url_name': 'contact'},
#                            {'title': "Войти", 'url_name': 'login'},
#                            ]
#         return context


def index(request):
    group_test = Test_group.objects.all()
    test_title = Test_title.objects.all()

    context = {
        'group_test': group_test,
        'test_title': test_title,
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


def show_tests(request, test_id):
    tests = Test_title.objects.filter(tests_id=test_id)  # исправить
    test_title = Test_title.objects.get(pk=test_id)  # исправить
    context = {
        'tests': tests,
        'menu': menu,
        'title': test_title,
    }

    return render(request, 'testsite/show_test.html', context=context)

# class ShowTest(ListView):
#     model = Test_title
#     template_name = 'testsite/show_test.html'
#     context_object_name = 'test_name'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = Test_title.objects.get(pk=self.kwargs['test_id'])
#         context['menu'] = [{'title': "О сайте", 'url_name': 'about'},
#                            {'title': "Все тесты", 'url_name': 'all_tests'},
#                            {'title': "Обратная связь", 'url_name': 'contact'},
#                            {'title': "Войти", 'url_name': 'login'},
#                            ]
#         return context
#
#     def get_queryset(self):
#         return Test_title.objects.filter(id=self.kwargs['test_id'])

# def show_group_test(request, group_test_id):
#     group_test = Test_group.objects.filter(group_test_id=group_test_id)
#     test_title = Test_title.objects.all()
#
#     context = {
#         'group_test': group_test,
#         'test_title': test_title,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'group_test_selected': group_test_id,
#     }
#
#     return render(request, 'testsite/index.html', context=context)
