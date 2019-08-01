from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    gender =(
        ('male','男'),
        ('female','女')
    )
    account_number = models.CharField(max_length=20,blank=False)
    name = models.CharField(max_length=10,blank=False)
    gender = models.CharField(max_length=10,choices=gender,default='male')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15,blank=False)
    createdate = models.DateTimeField(default=timezone.now)

