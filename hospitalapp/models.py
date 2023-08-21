from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)