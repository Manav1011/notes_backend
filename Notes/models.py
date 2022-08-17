from django.db import models
from accounts.models import UserEmail

# Create your models here.


class UserNotes(models.Model):
    title=models.CharField(max_length=255,default='No Title')
    content=models.TextField(blank=True,null=True)
    user=models.ForeignKey(UserEmail, related_name='user_notes',on_delete=models.CASCADE)
    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    