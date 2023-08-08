from django.urls import path

from tcsloral import views
urlpatterns = [
    path('',views.index),
    path('question/<int:group_num>/<int:question_num>/',views.group_question),
    path('answer/<int:group_num>/<int:question_num>/',views.answer),
    path('about/',views.about),
]
