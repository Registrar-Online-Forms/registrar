from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def signUp(request):
    #TO DO
    user = {'firstname': 'John', 'lastname': 'Doe'}
    context = {
        'user': user
        }
    return render(request, 'signUp.html', context)

def login(request):
    #TO DO
    user = {'firstname': 'John', 'lastname': 'Doe'}
    context = {
        'user': user
        }
    return render(request, 'login.html', context)

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

def newForm(request):
    user = {'firstname': 'John'} # This is only needed to show "Welcome [Student]" - Ben
    context = {
        'user': user
        }
    return render(request, 'newForm.html',context)

def help(request): # So for this page I replaced the "Welcome [Student]" greeting to skip having to request anything from the database - Ben
    return render(request, 'help.html')

def history(request):  
    # Copy/Pasted from Index, replace with actual values once database online
    user = {'firstname': 'John', 'lastname': 'Doe'}
    
    one = {'formType': 'Change Adivsor', 'submission' : '1/23/2023', 'status': 'Pending'}
    two = {'formType': 'Drop/Add Class', 'submission' : '1/2/2022', 'status': 'Awaiting Registrar Approval'}
    three = {'formType': 'Drop/Add Class', 'submission' : '12/23/2022', 'status': 'Awaiting Advisor Approval'}
    four = {'formType': 'Drop/Add Major', 'submission' : '10/10/2022', 'status': 'Complete'}
    recents = {'one': one, 'two': two, 'three': three, 'four': four}
    context= {
        'user': user,
        'recents': recents
        }
    return render(request, 'history.html', context)