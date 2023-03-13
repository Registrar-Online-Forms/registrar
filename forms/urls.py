from django.urls import path
import urllib3

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addDropClass', views.addDropClass, name='addDropClass'),
    path('registrar', views.registrar, name='registrar'),
    path('professor', views.professor, name='professor')
]

