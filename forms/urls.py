from django.urls import path

from . import views

# usage: path('the name of the page in the url', where to find the page in views.py, the name of the page)

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('signUp', views.signUp, name='signUp'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('addDropClass', views.addDropClass, name='addDropClass'),
    path('new', views.newForm, name='newForm'),
    path('help', views.help, name='help'),
    path('history', views.history, name='history')
]