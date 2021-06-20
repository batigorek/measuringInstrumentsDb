from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/instruments/calipers', views.index, name='calipers'),
    path('/instruments/micrometers', views.index, name='micrometers')
]