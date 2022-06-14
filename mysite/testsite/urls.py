from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('all_tests/', all_tests, name='all_tests'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('test_group/<int:test_group_id>/', show_tests, name='tests'),
    path('test_group/<int:test_group_id>/<int:questions_id>', show_questions, name='questions'),
]
