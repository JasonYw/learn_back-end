from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app import models


def test(request):
    #python .\manage.py createsuperuser 创建django超级用户
    # models.Userinfo.objects.create(username="root",email="qqqqqq")
    # models.Userinfo.objects.create(username="root",email="qqqqqq",ctime='2011-01-01')
    # return HttpResponse('200')
    return render(request,'test.html',{
        "k":{'k1':'v1','k2':'v2'},
        "name":"hhhhhh",
    })


def checklogin(func):
    def wrap(request):
        v =request.session.get("username")
        if v:
            return func(request)
        else:
            return redirect('/login/')
    return wrap


def session_login(request):
    '''
    可以有多个cookie键值对
    response =HttpResponse('200')
    response.set_cookie('k1','v1')
    response.set_cookie('k2','v2')
    response.set_cookie('k3','v3')
    return response
    '''
    if request.method =="GET":
        return render(request,'login.html')
    if request.method =="POST":
        u =request.POST.get("user")
        p =request.POST.get('password')
        if u=="root" and p=="0125":
            #1.生成随机字符串
            #2.通过cookie发送给客户端
            #3.在服务端保存{随机字符串：{'xxx':'....'}}
            request.session['username'] ='root' #此行可以完成上述三件事
            request.session['email'] ='root@root.com'
            '''
                {
                    随机字符串1：{'username':'root','email':''root@root.com',...}
                }
            django默认把这个随机字符串放在了数据库表里 django_session表中
            request.session['k1'].get 获取
            request.session['k1'] =xxx 设置
            request.session.setdefault('k1','11') 若不存在则设置
            del request.session['k1'] 删除k1key 以及k1的value

            request.session.keys()
            request.session.values()
            request.session.item()
            request.session.itemkeys()
            request.session.itemvalues()
            
            session_key =request.session.session_key 拿到的是随机字符串
        
            request.session.delete(session_key) 删除用户一切的数据以及对应的随机字符串，下次要重新登陆
            request.session.exists(session_key) 判断用户随机字符串是否存在
            request.session.clear_expired() 删除掉数据库里已经超时的session
            django默认随机字符串保存2周

            request.session.set_expiry(value) 设置超时间，在cookie中设置和存在数据库，单位秒
            #如果value是一个整数，session会在这些证书秒数后失效
            #如果value是个datetime或timedelta，session会在这个时间后失效
            #如果value是0，则关闭浏览器就会失效
            
            '''
            return redirect('/index/')
    return redirect('/login/')

@checklogin
def index(request):
    #1.获取客户端的cookie中的随机字符串
    #2.去session中查找有没有随机字符串
    #3.去session查看对应的key，并查看key对应的value是否有username
    # v =request.session.get('username') #此行可完成上述三件事
    # if v:
    return HttpResponse('SUCCESS')
    # else:
    #     return redirect('/login/')
# Create your views here.

   
