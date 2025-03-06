from django_filters import rest_framework as filters
from classes.models import ClassRoom


class ClassRoomFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    year = filters.NumberFilter(lookup_expr="icontains")
    min_year = filters.NumberFilter(field_name="year", lookup_expr="gte")
    max_year = filters.NumberFilter(field_name="year", lookup_expr="lte")

    class Meta:
        model = ClassRoom
        fields = ["name", "year"]
