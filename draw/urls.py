from django.contrib import admin
from django.urls import path

from draw.views import shape

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shapes/', shape, name='shape'),
]
