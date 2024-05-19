from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoUserProfile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    