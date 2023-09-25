from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class LinkPage(models.Model):
    title = models.CharField( max_length=50)
    #bgImage = models.ImageField(upload_to="backgrounds/", height_field=None, width_field=None, max_length=None)
    # url = models.TextField(default="youPage")
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
 
class Link(models.Model):
    linkPage = models.ForeignKey(LinkPage, on_delete=models.CASCADE)
    type = models.CharField( max_length=100,default="")
    url = models.URLField( max_length=200)
    color = models.CharField(max_length=7)