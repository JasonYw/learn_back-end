from django.shortcuts import render,HttpResponse,redirect
from app import models
from django.db.models import Q

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
            # request.session['username'] =userinfo.username
            # request.session['password'] =userinfo.password
            # request.session['sex'] =userinfo.sex
            request.session['user_info'] ={'user_name':userinfo.username,'user_password':userinfo.password,'user_sex':userinfo.sex}
            if session_delay == "save":
                request.session.set_expiry(604800)
            return redirect('/userindex/'+sex+'/'+username+'.html')
        else:
            return redirect('/login/')

def chek_login(func):
    def wrap(request,a=None,b=None):
        userinfo =request.session.get("username")
        if userinfo:
            return func(request,a,b)
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


@chek_login
def user_index(request,sex,username):
    '''
        !!!思想由于已经登录成功所以可以从session里面拿数据
    '''
    if sex == "male":
        all_list =models.Girl.objects.all()
        obj =models.Boy.objects.filter(username=username).first()
        date_list =obj.link_by_set.all().filter(boy_id_id =obj.id)
        #dictlist =models.Boy.objects.filter(username=username).values('girl_id__username')
        if date_list:
            targetlist =[]
            for date in date_list:
                targetlist.append(date.girl_id.name)
                print(date.girl_id.name)
    if sex == "female":
        all_list=models.Boy.objects.all()
        obj =models.Girl.objects.filter(username=username).first()
        #dictlist =models.Girl.objects.filter(username=username).values('boy_id__username')
        date_list =obj.link_by_set.all().filter(girl_id_id =obj.id)
        if date_list:
            targetlist =[]
            for date in date_list:
                targetlist.append(date.boy_id.name)
                print(date.boy_id.name)
    return render(request,'user_index.html',{"sex":sex,"user":obj,"datelist":targetlist,"alllist":all_list})
    
def add_date(request):
    if request.method == "POST":
        sex =request.POST.get("usersex")
        username =request.POST.get("username")
        targetname =request.POST.get("targetname")
        if request.POST.get("usersex") =="male":
            b_obj =models.Boy.objects.filter(username=username).first()
            g_obj =models.Girl.objects.filter(username=targetname).first()
            a,created =models.Link_by.objects.get_or_create(boy_id_id=b_obj.id,girl_id_id=g_obj.id,defaults={'boy_id_id':b_obj.id,'girl_id_id':g_obj.id})
        if request.POST.get("usersex") =="female":
            b_obj =models.Boy.objects.filter(username=targetname).first()
            g_obj =models.Girl.objects.filter(username=username).first()
            a,created =models.Link_by.objects.get_or_create(boy_id_id=b_obj.id,girl_id_id=g_obj.id,defaults={'boy_id_id':b_obj.id,'girl_id_id':g_obj.id})
        return HttpResponse("200")




def test(request):
    # models.Boy.objects.create(name="root1",username="root1",password="0125")
    # models.Boy.objects.create(name="root2",username="root2",password="0125")
    # models.Boy.objects.create(name="root3",username="root3",password="0125")
    # models.Girl.objects.create(name="g1",username="g1",password="0125")
    # models.Girl.objects.create(name="g2",username="g2",password="0125")
    # models.Girl.objects.create(name="g3",username="g3",password="0125")
    # models.Link_by.objects.create(boy_id_id=2,girl_id_id=2)
    # models.Link_by.objects.create(boy_id_id=2,girl_id_id=4)
    return HttpResponse('200ok')

def logout(request):
    if request.session.get('userinfo'): #删除前先做判断
        request.session.delete(request,session.session_key) #把数据库中的session删除
        request.session.clear() #设置cookie为超时

