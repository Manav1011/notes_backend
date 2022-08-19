from django.shortcuts import render
from .models import UserEmail, Token
from .serializers import TokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt
import json
import string
import random
from django.core.mail import send_mail
# Create your views here.


@api_view(['POST'])
def LoginOrSignupView(request):
    try:
        UserObj, emailcreated = UserEmail.objects.get_or_create(
            email=request.data['email'])
        N = 7
        random_string = ''.join(random.choices(string.ascii_lowercase +
                                               string.digits, k=N))
        try:
            UserObj.otp=random_string            
            email_from = 'manavshah1011.ms@gmail.com'
            email = json.dumps(request.data['email'])
            send_mail("OTP for account activation", f"Your OTP is :{random_string}", email_from, [email,], fail_silently=False)
            UserObj.save()
            return Response(random_string)
        except Exception as e:
            print(e)
            return Response('Please Enter Correct Email')
    except Exception as e:
        print(e)
        otp=request.data['otp']
        try:
            UserObj = UserEmail.objects.get(otp=otp)
            encoded_token = jwt.encode(
            {"token": UserObj.email+str(otp)}, "DjangoNotes", algorithm="HS256")
            data = {
                'token': encoded_token
            }
            TokenObj, tokencreated = Token.objects.get_or_create(email=UserObj)
            serializer = TokenSerializer(TokenObj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data)
            else:
                print(serializer.errors)
                return Response("Account Already Exists")
        except Exception as e:
            print(e)
            return Response("Invalid OTP!! Try Again")


# {
#     "email":"manavshah1011.ms@gmail.com"
# }
