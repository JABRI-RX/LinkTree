 
from django.urls import path
 
from .views import *
 
app_name = "LinkPage"
handler404 = 'LinkPage.views.handler404'
urlpatterns = [
    path("Browse",browse,name="browse"),
    path("createPage",createPage,name="createPage"),
    path("updatePage",updatePage,name="updatePage"),
    path("DeletePage",DeletePage,name="DeletePage"),
    path("page/<uuid:uuid>/",linkpage_details,name="linkpage_details")
     
]
