from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! you are at my Jangooo Home web")

def about(request):
    return HttpResponse("Hello! you are at my Jangooo about web")

def contact(request):
    return HttpResponse("Hello! you are at my Jangooo contact web")