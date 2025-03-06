from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50, unique=True)
    founded_date = models.DateField()
    address = models.CharField(max_length=100)
    principal = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
