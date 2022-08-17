from rest_framework import serializers
from .models import UserEmail,Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        fields=('token',)