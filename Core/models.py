from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class NewUserInfo(models.Model):
    userId = models.OneToOneField(User,on_delete=models.CASCADE)
    userBio = models.TextField(blank=True)
