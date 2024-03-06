from django.urls import path
from .views import feedback, thankyou

urlpatterns = [
    path("", feedback, name="feedback"),
    path("thankyou", thankyou, name="thankyou"),
]
