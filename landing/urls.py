from django.urls import path
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', views.index),
    path('something/', views.second),
]