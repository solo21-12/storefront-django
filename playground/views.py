from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def say_hello(request: HttpRequest) -> HttpResponse:
    return render(request, "hello.html", {"name": "Dawit"})
    # return HttpResponse("hello world")
