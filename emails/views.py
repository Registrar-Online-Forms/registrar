from django.shortcuts import render
from django.core.mail import EmailMessage

# Email Sender
#Plcaeholder until form functions are implemented
from django.http import HttpResponse

def index(request): #Handels request for page, sends email everytime it is loaded
    sendFormSubmitEmail('colleendoran314@gmail.com')
    return HttpResponse("Welcome to the email sender! Your email has been sent.")

def sendFormSubmitEmail(to): # to is email address recieving the email
    msg = EmailMessage('No-reply Form Submition Confirmation',
                        'Congratulations, your form has been submitted! \nPlease view the "Form History" section to veiw your subbmitted form. \n\n - Registrar Portal',
                        to = [to])
    msg.send()

def sendSignitureRecievedEmail(to): # to is email address recieving the email
    msg = EmailMessage('No-reply Signiture Confirmation',
                        'Thank you, your signiture has been received! \nPlease view the "Form History" section to veiw your subbmitted form. \n\n - Registrar Portal',
                        to = [to])
    msg.send()

def sendAlertEmail(to): # to is email address recieving the email
    msg = EmailMessage('No-reply New Form Notification',
                        'There has been a new form submitted to you that requires your attention. \nPlease view the "Pending Forms" section to veiw this form. \n\n - Registrar Portal',
                        to = [to])
    msg.send()
