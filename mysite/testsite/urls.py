from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('', ShowGroup.as_view(), name='home'),
    path('about/', about, name='about'),
    path('all_tests/', all_tests, name='all_tests'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('test_group/', show_tests, name='tests'),
    path('test_group/<int:test_group_id>/', show_tests, name='tests'),
    # path('tests/<int:test_id>/questions_in_test/', show_questions, name='questions_in_test')
    # path('tests/<int:group_title_id>/', ShowGroup.as_view(), name='group_tests')
]
