from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/show/
    path('show', views.show, name='show'),
    path('sure', views.sure, name='sure'),
    path('ans', views.ans, name='ans'),
]