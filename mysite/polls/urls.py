from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/polls/
    path('question', views.question, name='question'),
    path('answer', views.answer, name='answer'),
    path('where', views.where, name='where'),
]