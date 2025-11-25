from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail

User = get_user_model()

@receiver(pre_save, sender=User)
def before_saving_user(sender, instance, **kwargs):
    print("Before saving user")


@receiver(post_save, sender=User)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        print("New user created")
        user = User.objects.get(email="david@test.com")
        send_mail(
            "New User Created",
            f"New user {instance.email} created",
            "",
            [user.email],
            fail_silently=False,
        )
    else:
        print("User details updated")
