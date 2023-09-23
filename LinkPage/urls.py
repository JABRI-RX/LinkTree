 
from django.urls import path
 
from .views import *
 
app_name = "LinkPage"

urlpatterns = [
    path("Browse",browse,name="browse"),
    path("createPage",createPage,name="createPage"),
    path("updatePage",updatePage,name="updatePage"),
    path("DeletePage",DeletePage,name="DeletePage"),
     
]
