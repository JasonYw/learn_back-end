from django.shortcuts import render,HttpResponse,redirect
from app import models

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method =="POST":
        username =request.POST.get("username")
        password =request.POST.get("password")
        sex =request.POST.get("sex")
        session_delay =request.POST.get("save_session")
        if sex =="male":
            userinfo =models.Boy.objects.all().filter(username=username,password=password).first()
        if sex =="female":
            userinfo =models.Girl.objects.all().filter(username=username,password=password).first()
        if userinfo != None:
            request.session['username'] =userinfo.username
            request.session['password'] =userinfo.password
            if session_delay == "save":
                request.session.set_expiry(604800)
            return HttpResponse('test')
        else:
            return redirect('/login/')

def chek_login(func):
    def wrap(request):
        userinfo =request.session.get("username")
        if userinfo:
            return func(request)
        else:
            return redirect('/login/')
    return wrap

def register(request):
    if request.method =="POST":
        name =request.POST.get("name")
        username =request.POST.get("username")
        password =request.POST.get("password")
        sex =request.POST.get("sex")
        if sex=="male":
            models.Boy.objects.create(name=name,username=username,password=password)
        if sex=="female":
            models.Girl.objects.create(name=name,username=username,password=password)
        return HttpResponse('200')
