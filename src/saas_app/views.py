from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('about page')