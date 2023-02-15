from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    # user is an object variable with firstname and lastname attributes
    user = {'firstname': 'John', 'lastname': 'Doe'}
    # context is a dictionary variable with key 'user' and value user
    # this references the user object variable
    # and passes it to the web page. Variables in the web page are referenced by {{objectname.attribute}}
    one = {'formType': 'Change Adivsor', 'submission' : '1/23/2023', 'status': 'Pending'}
    two = {'formType': 'Drop/Add Class', 'submission' : '1/2/2022', 'status': 'Awaiting Registrar Approval'}
    three = {'formType': 'Drop/Add Class', 'submission' : '12/23/2022', 'status': 'Awaiting Advisor Approval'}
    four = {'formType': 'Drop/Add Major', 'submission' : '10/10/2022', 'status': 'Complete'}
    recents = {'one': one, 'two': two, 'three': three, 'four': four}
    context= {
        'user': user,
        'recents': recents
        }
    return render(request, 'index.html', context)

def addDropClass(request):
    user = {'firstname': 'John', 'lastname': 'Doe'}
    context = {
        'user': user
        }
    return render(request, 'addDropClass.html',context)
