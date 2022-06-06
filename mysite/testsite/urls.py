from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('', ShowGroup.as_view(), name='home'),
    path('about/', about, name='about'),
    path('all_tests/', all_tests, name='all_tests'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('tests/<int:test_id>/', show_tests, name='tests'),
    # path('tests/test_name/<int:test_name_id>', test_name, name='test_name')
    # path('tests/<int:group_title_id>/', ShowGroup.as_view(), name='group_tests')
]
