from django.db import models
from school.models import School
from django.core.validators import MinValueValidator, MaxValueValidator


class ClassRoom(models.Model):
    name = models.CharField(verbose_name="Class Name", max_length=50, unique=True)
    subject = models.CharField(
        verbose_name="Subject",
        max_length=50,
        null=False,
        blank=False,
    )
    year = models.IntegerField(verbose_name="Year")
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="classes",
    )
    students = models.ManyToManyField(
        "accounts.User",
        related_name="classes",
    )
    courses = models.ManyToManyField("Course", related_name="classes")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
