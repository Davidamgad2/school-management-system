import logging
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):

    def process_request(self,request):
        logger.info(f"Request {request.method} {request.path}")
        print(f"Request Headers: {request.headers}")
        if request.headers.get("x"):
            return HttpResponse("not valid")
        return None

    def process_response(self,request,response):
        logger.info(f"response : {response}, {response.status_code}")
        if getattr(request, 'x', None):
            print("Hello David")
        return response
