from django.urls import path
import urllib3

from . import views

# usage: path('the name of the page in the url', where to find the page in views.py, the name of the page)

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.registrar, name='registrar'),
    path('professor', views.professor, name='professor'),
    path('new', views.newForm, name='newForm'),
    path('help', views.help, name='help'),
    path('history', views.history, name='history'),
    path('addDropClass', views.addDropClass, name='addDropClass'),
    path('declareMajor', views.declareMajor, name='declareMajor'),
    path('declareMinor', views.declareMinor, name='declareMinor'),
    path('dropMajor', views.dropMajor, name='dropMajor'),
    path('dropMinor', views.dropMinor, name='dropMinor'),
    path('auditToCredit', views.auditToCredit, name='auditToCredit'),
    path('creditToAudit', views.creditToAudit, name='creditToAudit'),
    path('overload', views.overload, name='overload'),
    path('requestPassNoPass', views.requestPassNoPass, name='requestPassNoPass'),
    path('internshipContract', views.internshipContract, name='internshipContract'),
    path('changeAdvisor', views.changeAdvisor, name='changeAdvisor')

]

#list of forms
#addDropClass
#declareMajor
#declareMinor
#dropMajor
#dropMinor
#auditToCredit
#creditToAudit
#overload
#requestPassNoPass
#internshipContract
#changeAdvisor