from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def feedback(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "feedback_app/feedback.html")


def thankyou(request):
    return render(request, "feedback_app/thankyou.html")
