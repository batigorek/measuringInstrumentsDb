from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/calipers', views.index, name='calipers'),
    path('/micrometers', views.index, name='micrometers')
]