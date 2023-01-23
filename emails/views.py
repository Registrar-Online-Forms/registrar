from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.http import HttpResponse

def index(request):
    send_mail('IT WORKS!',
        'THANK THE LORD!',
        'dora3649@ravens.benedictine.edu',
        ['colleendoran314@gmail.com'],
        fail_silently=False)
    return HttpResponse("Welcome to the email sender! Your email has been sent.")