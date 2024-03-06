from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage


# Create your views here.
def feedback(request):
    if request.method == "POST":
        data = request.POST
        email = data["email"]
        message = data["message"]
        mail_subject = "Thanks for the feedback"
        mail_message = "Thanks for the feedback"
        email_obj = EmailMessage(mail_subject, mail_message, to=[email])
        if email_obj.send():
            print("Success: Email sent successfully")
        else:
            print("Failure: Email lost its way :(")
        return redirect("thankyou")
    return render(request, "feedback_app/feedback.html")


def thankyou(request):
    return render(request, "feedback_app/thankyou.html")
