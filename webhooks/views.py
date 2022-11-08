from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def webhooksview(request):    
    if request.method == 'GET':
        return HttpResponse(request.GET['hub.challenge'])
    else:
        print(json.loads(request.body))
        return HttpResponse("Success")    
        
