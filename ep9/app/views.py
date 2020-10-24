from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form
from django.forms import fields



class LoginForm(Form):
    username =fields.CharField(
        required=True,
        min_length=3,
        max_length=15,
        error_messages ={
            "required":"用户名不能为空",
            "min_length":"用户名小于最小长度",
            "max_length":"用户名大于最大长度"
        }
    )
    password =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码不能为空",
            "min_length":"密码小于最小长度",
            "max_length":"密码大于最大长度"
        }
    )
    
class RegisterForm(LoginForm):
    password_again =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码前后不一致",
            "min_length":"密码前后不一致",
            "max_length":"密码前后不一致",
        }
    )

    


def login(request):
    if request.method =="GET":
        return render(request,"login.html")
    if request.method =="POST":
        logininfo =LoginForm(request.POST)
        if logininfo.is_valid():
            if logininfo.cleaned_data.get("username") =="root" and logininfo.cleaned_data.get("password")=="0125":
                return HttpResponse("200")
            return render(request,"login.html",{"wrong":"用户名密码错误"})
        else:
            return render(request,"login.html",{"obj":logininfo})

def register(request):
    registerinfo =RegisterForm(request.POST)
    if registerinfo.is_valid():
        print(registerinfo.cleaned_data)
        if registerinfo.cleaned_data.get("password") == registerinfo.cleaned_data.get("password_again"):
            return HttpResponse("200")
    return redirect("/login/")