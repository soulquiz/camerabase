from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

def detail(request, event_id):
    return HttpResponse("you're looking at event %s." % event_id)

def live_steam(request):
    return HttpResponse("you're watching live steam")

def setting_mode(request):
    return HttpResponse("you're watching setting mode")
