from django.urls import path
import urllib3

from . import views

# usage: path('the name of the page in the url', where to find the page in views.py, the name of the page)

urlpatterns = [
    path('', views.index, name='index'),
    path('addDropClass', views.addDropClass, name='addDropClass'),
    path('registrar', views.registrar, name='registrar'),
    path('professor', views.professor, name='professor')
    path('new', views.newForm, name='newForm'),
    path('help', views.help, name='help'),
    path('history', views.history, name='history')
]

