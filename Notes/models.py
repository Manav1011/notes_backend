from django.db import models
from accounts.models import UserEmail
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class UserNotes(models.Model):
    title=models.CharField(max_length=255,default='No Title')
    content=models.TextField(blank=True,null=True)
    user=models.ForeignKey(UserEmail, related_name='user_notes',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    
@receiver(post_save,sender=UserNotes)
def PreSaveContentCheck(sender,instance,*args,**kwargs):
    if not instance.content:
        instance.delete()        