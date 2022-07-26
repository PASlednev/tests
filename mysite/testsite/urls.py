from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('all_tests/', all_tests, name='all_tests'),
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('test_group/<int:test_group_id>/', show_tests, name='tests'),
    path('test_group/<int:test_group_id>/<int:test_id>', show_testing, name='show_test'),
    # path('testing/', show_testing, name='show_testing')
]
