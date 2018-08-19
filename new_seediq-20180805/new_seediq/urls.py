from django.urls import path
from . import views

urlpatterns = [
    path('search_form',views.search_form),
    path('search_result',views.search_result),
]
