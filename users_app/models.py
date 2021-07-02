from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)