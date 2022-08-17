from django.contrib import admin
from .models import UserEmail,Token
# Register your models here.

admin.site.register(UserEmail)
admin.site.register(Token)
