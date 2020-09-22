"""ep2_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(
        request,
        'index/index.html',
        {
            'name':'alxe',
            'users':['apple','lijie'],
            'user_dict':{'k1':'v1','k2':'v2'},
            'user_list_dict':[
                {'id':1,'name':'alex','email':'aaa@a.com'},
                {'id':2,'name':'tom','email':'bbb@a.com'},
            ]
        }
    )

def login(request):
    '''
        处理用户请求，并返回其内容
        request:用户请求相关的所有信息（对象），此request是django已经处理好的
        HttpResponse('字符串') 只支持字符串 response为字符串
        render(request,'文件地址') 支持文件 response为文件中的字符串， 相当于 f=open();HttpResponse(f.read())
        redirect() 用于页面重定向，跳转
    '''

    #不可以直接返回字符串，需要导入from django.shortcuts import HttpResponse
    #通过HttpResponse来返回
    #用户将看到HttpResponse的参数，本质也是字符串
    #HttpResponse 参数只支持字符串
    #return HttpResponse('login.html')

    #request.method 拿到请求的类型 GET POST PUT 。。。
    print(request.method)

    if request.method  == "GET":
        #自动找到模板路径下的login.html文件，读取内容并返回给用户，模板配置在setting.py中
        #render内部也调用了HttpResponse最终返回
        return render(request,'login.html')
    else:
        #request.POST 用户POST时提交的数据，本质时request请求体里面的东西
        print(request.POST)

        #不要直接用索引的方式取dict 若前端没有username，password 会报错，用.get则可以避免报错
        u =request.POST.get('username')  
        p =request.POST.get('password')
        if u=='root' and p=='0125':
            return redirect('/index/')
        else:
            #django里面集成了模板渲染器也就是jinja2，render第三个参数就是替换html中特殊的字符，用的就是jinja2模块
            return render(request,'login.html',{'message':'wrong id or password'})


urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'login/',login),
    path(r'index/',index),
]
