from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import AnswersForm, UserRegisterForm, UserLoginForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Все тесты", 'url_name': 'all_tests'},
        {'title': "Обратная связь", 'url_name': 'contact'},
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


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'testsite/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


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

# class Show_testing(TemplateView):
#     template_name = 'testsite/show_questions.html'
#
#     def testing(request, test_group_id, test_id):
#         que = Question.objects.filter(test_title__pk=test_group_id)
#         paginator = Paginator(que, 1)
#         page_num = request.GET.get('page', 1)
#         page_object = paginator.get_page(page_num)
#         que_id = page_object.object_list[0].id # дописать проверку на наличие нулевого элемента
#         ans = Answer.objects.filter(question__pk=que_id).values('answer_text', 'question__id').order_by('question_id')
#         context = {'page_obj': page_object,
#                    'que': que,
#                    'ans': ans,
#                    'test_group_id': test_group_id,
#                    'test_id': test_id,
#                    }
#
#     def get(self, request, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = AnswersForm(request.POST)
#         context.update({'form': form})
#         return self.render_to_response(context)
#
#     def post(self, request, *args, **kwargs):
#         form = AnswersForm(self.request.POST)
#         if form.is_valid():
#             form_update = form.save(commit=False)
#             #form_update.related_user = request.user
#             form_update.save()
#             return HttpResponseRedirect(reverse_lazy('home'))
#         else:
#             print('NotValid')
#             return self.form_invalid(form, **kwargs)
#
#
#     def form_invalid(self, form, **kwargs):
#         context = self.get_context_data()
#         context.update({'formOne': form})
#         return self.render_to_response(context)


def show_testing(request, test_group_id, test_id):
    que = Question.objects.filter(test_title__pk=test_group_id)
    paginator = Paginator(que, 1)
    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)
    que_id = page_object.object_list[0].id  # дописать проверку на наличие нулевого элемента
    ans1 = Answer.objects.filter(question_id=que_id)
    print(ans1[0])
    ans = Answer.objects.filter(question__pk=que_id).values('answer_text', 'question__id').order_by('question_id')
    if request.method == 'POST':
        form = AnswersForm(request.POST)
        form.fields['answer_text'].choices = [('F', ans1[0]), ('S', ans1[1]), ('T', ans1[2])]
        if form.is_valid():
            answer = form.save(commit=False)
            return redirect(answer)
    else:
        form = AnswersForm()
    context = {'page_obj': page_object,
               'form': form,
               'que': que,
               'ans': ans,
               'test_group_id': test_group_id,
               'test_id': test_id,
               }
    return render(request, 'testsite/show_questions.html', context)

