from django.core.mail import EmailMessage
from celery import shared_task
from time import sleep


@shared_task()
def send_email(to_email):
    sleep(10)
    mail_subject = "Thanks for the feedback"
    mail_message = "Thanks for the feedback"
    email_obj = EmailMessage(mail_subject, mail_message, to=[to_email])
    if email_obj.send():
        print("Success: Email sent successfully")
    else:
        print("Failure: Email lost its way :(")
