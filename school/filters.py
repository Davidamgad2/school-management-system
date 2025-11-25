import django_filters
from school.models import School
class SchoolFilter(django_filters.FilterSet):

    class Meta:
        model= School
        fields ={
            "name":["exact","icontains"]
        }