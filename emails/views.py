from django.shortcuts import render
from django.core.mail import EmailMessage

# Email Sender
#Placeholder until form functions are implemented
from django.http import HttpResponse
from datetime import datetime

def index(request): #Handels request for page, sends email everytime it is loaded
    sendFormSubmitEmail(['colleendoran314@gmail.com'], "Add Major", "0001", "Dr. tenBroek")
    sendSignitureRecievedEmail(['colleendoran314@gmail.com'], "Add Major", "0001")
    sendAlertEmail(['colleendoran314@gmail.com'], "0001")
    return HttpResponse("Welcome to the email sender! Your email has been sent.")

# recipients is an array of email addresses recieving the email
# formType is a string of the kind of form that is submitted
# submitID is a string(or int?) that identifies the form
# sentTo is a string of who is next in the authorization chain (aka, who gets the notification that their action is required)
def sendFormSubmitEmail(recipients, formType, submitID, sentTo): 
    now = datetime.now() #clock
    # mm/dd/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S") #gets time
    msg = EmailMessage('No-reply Form Submition Confirmation',
                    '''Congratulations, your form has been submitted!
                    \nPlease view the "Form History" section to veiw your subbmitted form.\n
                    \nSubmition Details:
                    \nForm: ''' + formType + '''
                    \nSent to: ''' + sentTo + '''
                    \nSubmission ID: ''' + submitID + '''
                    \nDate and Time of Submission: ''' + dt_string + '''\n
                    \n- Registrar Portal''',
                        to = recipients)
    msg.send()

def sendSignitureRecievedEmail(recipients, formType, submitID): #test
    now = datetime.now() #clock
    # mm/dd/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S") #gets time
    msg = EmailMessage('No-reply Signiture Confirmation',
                        '''Thank you, your signiture has been received! 
                        \nPlease view the "Form History" section to veiw your subbmitted form. \n
                        \nForm Details:
                        \nForm: ''' + formType + '''
                        \nSubmission ID: ''' + submitID + '''
                        \nDate and Time of Signiture: ''' + dt_string + '''\n
                        \n - Registrar Portal''',
                        to = recipients)
    msg.send()

def sendAlertEmail(recipients, submitID):
    msg = EmailMessage('No-reply New Form Notification',
                        '''There has been a new form submitted to you that requires your attention. 
                        \nPlease view the "Pending Forms" section to veiw this form. \n
                        \nRequires Attention:
                        \nsubmitID: ''' + submitID + '''\n
                        \n - Registrar Portal''',
                        to = recipients)
    msg.send()
