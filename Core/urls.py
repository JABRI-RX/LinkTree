 
from django.urls import path
 
from .views import *
 
app_name = "Core"
urlpatterns = [
    path('',index,name="home"),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path("forgotPassword/",forgotPassword,name="forgotPassword"),
    path("UserProfile",edit_user,name="edit_user"),
    path("ChangePassword",change_password,name="change_password"),
    path("logout",logout,name="logout"),
]
