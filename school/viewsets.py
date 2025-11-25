from rest_framework import viewsets
from school.models import School
from school.serializers import SchoolSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from school.filters import SchoolFilter
from rest_framework.decorators import action
from rest_framework.response import Response

class SchoolViewSet(viewsets.ModelViewSet):

    queryset= School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes= [IsAuthenticated]
    filterset_class = SchoolFilter
    
    @action(detail=False,methods=['get'],url_path="count")
    def statistics(self, request):
        schools = School.objects.count()
        return Response({"schools_count":schools})