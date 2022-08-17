from django.shortcuts import render
from .models import UserEmail,Token
from .serializers import TokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt
import json
import string
import io
import random
# Create your views here.

@api_view(['POST'])
def LoginOrSignupView(request):
    UserObj,emailcreated=UserEmail.objects.get_or_create(email=request.data['email'])    
    TokenObj,tokencreated=Token.objects.get_or_create(email=UserObj)
    print(TokenObj)
    print(str(tokencreated))
    N = 7
    print(UserObj)
    random_string = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=N))
    email=json.dumps(request.data['email'])
    encoded_token=jwt.encode({"token":email+str(random_string)},"DjangoNotes",algorithm="HS256")
    data={        
        'token':encoded_token        
    }
    
    serializer=TokenSerializer(TokenObj,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data)
    else:
        print(serializer.errors)
        return Response("Account Already Exists")


