from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import QuestionsForm, UserRegisterForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Все тесты", 'url_name': 'all_tests'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        {'title': "Зарегистрироваться", 'url_name': 'register'}
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


def show_tests(request, test_group_id):
    tests = Test_title.objects.filter(tests_id=test_group_id)
    test_title = Test_title.objects.get(pk=test_group_id)

    context = {
        'tests': tests,
        'menu': menu,
        'title': test_title,
    }
    return render(request, 'testsite/show_test.html', context=context)


def about(request):
    return render(request, 'testsite/about.html', {'menu': menu, 'title': 'О сайте'})


def all_tests(request):
    return HttpResponse("Все тесты")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return render(request, 'testsite/login.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'testsite/register.html', {"form": form})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_questions(request, test_group_id, test_id):
#     tests = Test_title.objects.filter(tests_id=test_group_id)
#     ans = Answer.objects.all()
#     que = Question.objects.filter(id__in=ans)
#     ans1 = Answer.objects.all()
#     return render(request, 'testsite/show_questions.html',
#                   {'tests': tests, 'que': que, 'ans1': ans1})


def show_testing(request, test_group_id, test_id):
    que = Question.objects.filter(test_title__pk=test_group_id)
    paginator = Paginator(que, 1)
    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)
    que_id = page_object.object_list[0].id  # дописать проверку на наличие нулевого элемента
    ans = Answer.objects.filter(question__pk=que_id).values('answer_text', 'question__id').order_by('question_id')
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(**form.cleaned_data)
            return redirect(question)
    else:
        form = QuestionsForm()
    context = {'page_obj': page_object,
               'form': form,
               'que': que,
               'ans': ans
               }
    return render(request, 'testsite/show_questions.html', context)
