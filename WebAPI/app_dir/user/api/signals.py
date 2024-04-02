from django.dispatch.dispatcher import receiver
import django.dispatch

from django.conf import settings
from django.core.mail import send_mail



welcome_email = django.dispatch.Signal(providing_args=["username","email","request"])
@receiver(welcome_email)
def welcome_email_send(sender,username,email,*args,**kwargs):
    print('sending email')
    subject = 'welcome to SCMS'
    message = f'Hi {username}, thank you for registering in SCMS.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )
