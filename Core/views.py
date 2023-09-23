from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import NewUserInfo
# Create your views here.
def index(request):
    return render(request,"core/index.html",{})

def login(request):
    if request.method == "POST":
            
        email = request.POST.get("email")
        password  = request.POST.get("password")
        try:
            user = User.objects.get(email=email,password=password)
            
            if user.is_active:
                auth_login(request,user)
                return render(request,"core/index.html",{})
        except Exception as error: 
            mode = 1
            print("exception is fucked right in the ass",error)
            return render(request,"core/login.html",{"mode":mode})
    else:
        return render(request,"core/login.html",{})
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        
        res = {}
        if User.objects.filter(email=email):
            print("Email Already Exists FGT")
            res["mode"] = 3
        elif password != password1:
            print("password arenot the same")
            res["mode"] = 1
        else:
            user = User.objects.create_user(username,email)
            user.password = password
         
            user_bio = NewUserInfo(userId=user)
            print(f"user created with id {user.pk}:{user.id}")
            print(f"UserInfo Created With Id {user_bio.id}")

            res["mode"] = 2
            user.save()
            user_bio.save()
        return render(request,"core/signup.html",{"res":res})
    else:
       
        return render(request,"core/signup.html",{})

def forgotPassword(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
    
            EmailMessage(
                subject="Password Reset",
                body="<b>The Password For your Account Is "+user.password,
                from_email="carti.youness65@gmail.com",
                to=[email]
            ).send()
        else:
            print(email)
            print(User.objects.all().values())
    return render(request,'core/forgot_pass.html',{})

def change_password(request):
    mode = None # 1 password changed #2 password is wrong #3 password aren't the same
    if request.method == "POST":
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        confpassword = request.POST.get("confpassword")
        try:
           
            user = User.objects.get(id=request.user.id,password=oldpassword)
            if newpassword == confpassword:
                user.password = newpassword
                user.save()
                mode = 1
            else:
                print(f"{newpassword}=={confpassword}")
                mode = 3
        except Exception as error:
            mode = 2
            print(f"The error is [{error}]")
    return render(request,"core/change_password.html",{"mode":mode})

def edit_user(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        bioText = request.POST.get("bio")
        #
        user = User.objects.get(id=request.user.id)
        userInfo = NewUserInfo.objects.get(userId=request.user.id)

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        userInfo.userBio = bioText

        user.save()
        userInfo.save()

        print(user)

    bio = NewUserInfo.objects.get(userId=request.user.id)
    return render(request,"core/edit_user.html",{"bio":bio.userBio})
        

@login_required()
def logout(request):
    auth_logout(request) 
    return render(request,"core/index.html",{})
 