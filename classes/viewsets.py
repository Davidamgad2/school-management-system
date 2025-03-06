from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from classes.models import ClassRoom
import json
from django.forms.models import model_to_dict
from rest_framework import viewsets
from .serializers import ClassRoomSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action


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
    # renderer_classes = [JSONRenderer]
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
