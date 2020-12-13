from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "testing/index.html")

def ansel(request):
    return HttpResponse("Hello, Ansel!")

def greet(request, name):
    return render(request, "testing/greet.html", {
        "name": name.capitalize()
    })