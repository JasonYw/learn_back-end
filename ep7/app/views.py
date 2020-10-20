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
            request.session['sex'] =userinfo.password
            if session_delay == "save":
                request.session.set_expiry(604800)
            return redirect('/userindex/'+sex+'/'+username+'.html')
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

def user_index(request,sex,username):
    if sex == "male":
        all_list =models.Girl.objects.all()
        obj =models.Boy.objects.filter(username=username).first()
        date_list =obj.link_by_set.all().filter(boy_id_id =obj.id)
        if date_list:
            targetlist =[]
            for date in date_list:
                targetlist.append(date.girl_id.name)
                print(date.girl_id.name)
    if sex == "female":
        all_list=models.Boy.objects.all()
        obj =models.Girl.objects.filter(username=username).first()
        date_list =obj.link_by_set.all().filter(girl_id_id =obj.id)
        if date_list:
            targetlist =[]
            for date in date_list:
                targetlist.append(date.boy_id.name)
                print(date.boy_id.name)
    return render(request,'user_index.html',{"user":obj,"datelist":targetlist,"alllist":all_list})
    
    

def test(request):
    # models.Link_by.objects.create(boy_id_id=2,girl_id_id=2)
    # models.Link_by.objects.create(boy_id_id=2,girl_id_id=4)
    return HttpResponse('200ok')

