from django.shortcuts import render
from rest_framework import generics
from .models import UserNotes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import UserEmail,Token
from .serializers import NoteSerializer
from accounts.models import Token


# Create your views here.


@api_view(['GET'])
def ListNotesView(request):
    try:
        auth_token=request.headers['AuthToken']    
    except Exception as e:
        return Response("Auth Token Not Valid")
    TokenObj=Token.objects.get(token=auth_token)
    UserObj=UserEmail.objects.get(email=TokenObj.email)
    NotesObj=UserNotes.objects.filter(user=UserObj).values().order_by('-updated')
    if NotesObj.count() <= 0:
        return Response(NotesObj)
    else:
        JsonObj=[]
        for i in NotesObj:
            if not i['content']:
                UserNotes.objects.get(id=i['id']).delete()
            else:
                JsonObj.append(i)
        return Response(JsonObj)
        

@api_view(['POST'])
def CreateNoteView(request):    
    try:
        auth_token=request.headers['AuthToken']    
    except Exception as e:
        return Response("Auth Token Not Valid")
    if request.method == 'POST':
        try:
            TokenObj=Token.objects.get(token=auth_token)
            UserObj=UserEmail.objects.get(email=TokenObj.email)
            data=request.data
            NotesObj=UserNotes.objects.create(user=UserObj,title=data['content'],content=data['content'])
            id=NotesObj.id   
            return Response(id)
        except:
            return Response('User Does Not Exits')

@api_view(['PATCH','DELETE','GET'])
def GetDeleteUpdateNotes(request,pk):
    try:
        auth_token=request.headers['AuthToken']        
    except Exception as e:
        return Response("Auth Token Not Valid")
    if request.method=='GET':
        try:
            NoteObj=UserNotes.objects.get(pk=pk)
            data={
                'id':NoteObj.id,
                'title':NoteObj.title,
                'content':NoteObj.content
            }
            return Response(data)
        except:
            return Response("Note Obj Not Found")
    if request.method=='DELETE':
        try:
            NoteObj=UserNotes.objects.get(pk=pk)
            NoteObj.delete()
            return Response("Deleted!!")
        except:
            return Response("Note Obj Not Deleted")
        
    if request.method=='PATCH':
        try:
            NoteObj=UserNotes.objects.get(pk=pk)
            data=request.data            
            if data['content']:                        
                serializer=NoteSerializer(NoteObj,data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response("Created!!")
                else:                    
                    return Response("Not Created!!")
            else:
                NoteObj.delete()
                return Response("Deleted!!")
        except Exception as e:
            print(e)
            return Response("Note Obj Not Found")
        
    
    
        
        




