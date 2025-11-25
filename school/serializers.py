from rest_framework import serializers

from school.models import School

class SchoolSerializer(serializers.ModelSerializer):
    school_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "founded_date",
            "address",
            "school_count"
        ]

    def validate_name(self,value):
        if not len(value) > 3:
            raise serializers.ValidationError("Name should be more than 3 ")
        return value

    def get_school_count(self,obj):
        return School.objects.count()

