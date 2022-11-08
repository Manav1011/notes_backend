from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def webhooksview(request):    
    print(request.GET)
    return HttpResponse(request.GET['hub_challenge'])
