from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from classes.models import ClassRoom, Course
import json
from django.forms.models import model_to_dict
from rest_framework import viewsets
from .serializers import ClassRoomSerializer, CourseSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Count, F, Q
import logging

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class ClassRoomView(View):
    def get(self, request, *args, **kwargs):
        class_rooms = ClassRoom.objects.all()
        if not class_rooms:
            return HttpResponse("No Classrooms")
        return HttpResponse(f"Hello, World!{class_rooms}")

    def post(self, request, *args, **kwargs):
        request_body = request.body.decode("utf-8")
        print(request_body)
        request.user
        object = ClassRoom(**json.loads(request_body))
        object.full_clean()
        object.save()
        return HttpResponse(f"Hello, World! POST {model_to_dict(object)}")

    def put(self, request, *args, **kwargs):
        print(self.kwargs.get("pk"))
        request_body = request.body.decode("utf-8")
        ClassRoom.objects.filter(id=self.kwargs.get("pk")).update(
            **json.loads(request_body)
        )
        object = ClassRoom.objects.get(id=self.kwargs.get("pk"))
        return HttpResponse(f"found {model_to_dict(object)}")

    def delete(self, request, *args, **kwargs):
        ClassRoom.objects.filter(id=self.kwargs.get("pk")).delete()
        return HttpResponse("Hello, World! DELETE")


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "year"]

    @action(
        detail=True,
        methods=["get"],
        url_path="say-hello",
        url_name="say",
    )
    def get_classroom(self, request, pk=None):
        pk = self.kwargs.get("pk")
        if pk:
            return Response(
                {"message": f"this is the class room {pk}"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "this is the class room"}, status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["get"],
        url_path="classes-aggregations",
        url_name="classes_aggregations",
    )
    def classes_aggregations(self, request, pk=None):
        _ = ClassRoom.objects.annotate(
            number_of_students=Count("students"),
            year_deducted=F("year") - 2,
        )
        logger.info("Classes Aggregations")
        logger.error("Classes Aggregations")

        _ = ClassRoom.objects.aggregate(total_students=Count("students"))

        _ = ClassRoom.objects.filter(
            Q(name__icontains="math") | Q(name__icontains="english")
        )
        ClassRoom.objects.bulk_create(
            [
                ClassRoom(name="Math", year=2021),
                ClassRoom(name="English", year=2021),
            ],
            10,
            ignore_conflicts=True,
            update_conflicts=True,
            update_fields=["name"],
        )
        _ = (
            ClassRoom.objects.all()
            .prefetch_related(
                "students"
            )  # To make the join in the quey instead of multiple queries with many to many and foreign key
            .select_related(
                "school"
            )  # To make the join in the quey instead of multiple queries with one to many and and one to one
        )


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        if serializer.is_valid():
            print("data", serializer.validated_data)
            Course.objects.bulk_create(
                [
                    Course(
                        code=data["code"],
                        title=data["title"],
                        description=data["description"],
                    )
                    for data in serializer.validated_data
                ],
                ignore_conflicts=False,
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
