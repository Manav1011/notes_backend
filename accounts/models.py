from django.db import models

# Create your models here.

class UserEmail(models.Model):
    email=models.EmailField(unique=True)    
    otp=models.CharField(max_length=7,null=True,blank=True)
    
    def __str__(self):
        return self.email
    
    
class Token(models.Model):
    token=models.TextField(null=True,blank=True)
    email=models.OneToOneField(UserEmail,on_delete=models.CASCADE,related_name='email_token')
    
    def __str__(self):
        return str(self.token)
    
