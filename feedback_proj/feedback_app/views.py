from django.http import HttpResponse
from django.shortcuts import redirect, render
from feedback_app.tasks import send_email


# Create your views here.
def feedback(request):
    if request.method == "POST":
        data = request.POST
        email = data["email"]
        message = data["message"]
        send_email.delay(email)
        return redirect("thankyou")
    return render(request, "feedback_app/feedback.html")


def thankyou(request):
    return render(request, "feedback_app/thankyou.html")
