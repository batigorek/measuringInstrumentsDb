from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.instruments_home, name='instruments_home'),
    path('micrometers', views.micrometers, name='micrometers'),
    path('calipers', views.calipers, name='calipers'),
    path('create_calipers', views.create_calipers, name='create_calipers'),
    path('create_micrometers', views.create_micrometers, name='create_micrometers'),
    path('calipers/<int:pk>/update_calipers', views.CalipersUpdateView.as_view(), name='calipers-update'),
    path('calipers/<int:pk>/delete_calipers', views.CalipersDeleteView.as_view(), name='calipers-delete'),
    path('micrometers/<int:pk>/delete_micrometers', views.MicrometersDeleteView.as_view(), name='micrometers-delete'),
    path('micrometers/<int:pk>/update_micrometers', views.MicrometersUpdateView.as_view(), name='micrometers-update'),
]