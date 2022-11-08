from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def webhooksview(request):    
    print(request.GET)
    print(request.POST)
    return HttpResponse(request.GET['hub.challenge'])
