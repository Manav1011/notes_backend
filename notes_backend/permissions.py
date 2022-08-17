from rest_framework import permissions
from rest_framework.response import Response

class TokenProvided(permissions.BasePermission):    
    message="Token Not Provided"
    def has_permission(self, request, view):
        if request.headers['Auth-Token']:            
            return True  
        else:
            return Response(self.message)

    def has_object_permission(self, request, view, obj):
        if request.headers['Auth-Token']:
            print("object Viewed:",request.headers['Auth-Token'])
            return True
        else:
            return Response(self.message)