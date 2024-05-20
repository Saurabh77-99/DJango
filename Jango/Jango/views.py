from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello! you are at my Jangooo Home web")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello! you are at my Jangooo about web")

def contact(request):
    return HttpResponse("Hello! you are at my Jangooo contact web")