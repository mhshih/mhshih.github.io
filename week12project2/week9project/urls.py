from django.contrib import admin
from django.urls import path

from week9project import views

urlpatterns = [
    path('index', views.index),
    path("results", views.output2),
    path("photo", views.photo),
    path("", views.home),
]
