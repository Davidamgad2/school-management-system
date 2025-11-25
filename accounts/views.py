from .tasks import send_welcome_email
from django.http import HttpResponse


def send_email(request):
    send_welcome_email.delay(1)
    return HttpResponse("Email sent")
