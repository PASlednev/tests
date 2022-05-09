from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path

from mysite import settings
from testsite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testsite.urls')),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
