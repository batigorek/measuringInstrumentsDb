from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.instruments_home, name='instruments_home'),
    path('micrometers', views.micrometers, name='micrometers'),
    path('calipers', views.calipers, name='calipers'),
]