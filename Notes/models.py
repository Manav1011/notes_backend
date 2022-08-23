from django.db import models
from accounts.models import UserEmail
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


# Create your models here.


class UserNotes(models.Model):
    title=models.CharField(max_length=255,default='No Title')
    content=models.TextField(blank=True,null=True)
    user=models.ForeignKey(UserEmail, related_name='user_notes',on_delete=models.CASCADE)    
    updated=models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.title)
    
    
@receiver(pre_save,sender=UserNotes)
def pre_save_receiver(sender,instance,*args,**kwargs):
    instance.updated = str(datetime.datetime.now()) 
    
    