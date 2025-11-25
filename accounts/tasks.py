from celery import shared_task
from accounts.models import User
import time


@shared_task
def send_welcome_email(user_id):
    try:
        _ = User.objects.get(id=user_id)
    except:
        pass
    print("Sending welcome email to user")
    time.sleep(10)
    return None
