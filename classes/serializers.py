from rest_framework.serializers import ModelSerializer
from .models import ClassRoom, Course
from rest_framework.validators import UniqueTogetherValidator


class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=ClassRoom.objects.all(),
                fields=["name", "year"],
                message="Classroom with this name and year already exists",
            )
        ]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
