from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def webhooksview(request):
    data = json.loads(request.body)    
    for i in data:
        print(i)
    return HttpResponse(data['hub_challenge'])
