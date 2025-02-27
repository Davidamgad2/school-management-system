from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(verbose_name="Class Name", max_length=50, unique=True)
    subject = models.CharField(verbose_name="Subject", max_length=50)
    year = models.IntegerField(verbose_name="Year")
