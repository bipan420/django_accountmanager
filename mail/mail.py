from django.core.mail import send_mail
from django.conf import settings

def send(subject = None, message=None,recipient_list=[]):
    email_from = settings.EMAIL_HOST
    try:
        send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)
        return True
    except:
        return False