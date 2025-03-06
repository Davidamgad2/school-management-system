from django.forms import ModelForm
from classes.models import ClassRoom
from django.core.exceptions import ValidationError


class ClassForm(ModelForm):
    # Field level validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise ValidationError("Name should be more than 3 characters")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get("subject")
        if len(subject) < 3:
            raise ValidationError("Subject should be more than 3 characters")
        return subject

    # form level validation
    def clean(self):
        clean_data = super().clean()
        name = clean_data.get("name")
        subject = clean_data.get("subject")
        if name == subject:
            raise ValidationError("Name and Subject should not be same")
        return clean_data

    class Meta:
        model = ClassRoom
        fields = ["name", "subject", "year"]
