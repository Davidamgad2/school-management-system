from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token


@csrf_exempt
def home(request, david):
    if request.method == "POST":
        print(request.body)
        return HttpResponse(f"Hello {david} POST")
    else:
        return HttpResponse(f"Hello {david}")


def retreive_classroom(request, class_name):
    context = {
        "title": class_name,
    }
    return render(request, "classes/index.html", context)


def csrf_obtain(request):
    csrf_token = get_token(request)
    return HttpResponse("CSRF, token {}".format(csrf_token))
