from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.urls import reverse
from app import models

# Create your views here.


def index(rquest):
    '''
        reverse 用来生成url
        urls 中 path('index/',views.index,name="n1")
        v等于/index/
    
        urls中 re_path(r'index/(\d+)',views.index,name="n1"),
        reverse('n1',args=(1,)) 生成/index/1

        urls中 re_path(r'index/(?P<a1>\d+)',views.index,name="n1"),
        reverse('n1',kwargs={'a1':111}) 生成/index/111

    '''
    user_list=[
        'alex','eric','tony'
    ]
    
    # v =reverse('n1',args=(1,)) 
    # v =reverse('n1',kwargs={'a1':111}) 
    # print(v)
    return render(rquest,'index.html',{'user_list':user_list})

# def edit(request):
#     return HttpResponse('....')
'''
re_path(r'edit/(\w+)/(\w+)/',views.edit) 第一在路由中的参数需要按照顺序
re_path(r'edit/(?P<a1>\w+)/(?P<a2>\w+)/',views.edit) 第二种不需要按照顺序，因为已经指定了 
以上两种 要统一用法！！！！，要不然会报错


re_path(r'edit/(\w+)/(?P<a2>\w+)/',views.edit) 搭配以下这种
def edit(request,a1,a2):这种会报错，会提示缺少一个参数a1
    print(a1,a2)
    return HttpResponse(a1+a2)

def edit(request,*args,**kwargs): 这种会报错，会提示缺少一个参数a2
    print(a1,a2)
    print(args,**kwargs)
    return HttpResponse(a1+a2)


re_path(r'edit/',views.edit) 表示 以edit/开头的url  搭配以下这种

# -*-coding:utf-8 -*-


def edit(request,*args,**kwargs): 不会报错 因为上面是正则表达式
    print(a1,a2)
    print(args,**kwargs)
    return HttpResponse(a1+a2)


re_path(r'edit$',views.edit) 表示 以edit开头的url 但是$为终止符，所以url只能是edit 推荐使用终止符


re_path(r'edit/(\w+).html$',views.edit) 只是一个正则表达式的模板，必须也要匹配上html 尤其是在html中
伪静态：
    -.html结尾的一般为静态网站
    -静态网站速度块，seo也会更高
    -动态网站拿到模板 再去数据库 在渲染 慢

'''
def edit(request,a1=None,a2=None):
    print(a1,a2)
    return HttpResponse(a1)


def login(request):
    return render(request,'login.html')



def orm(request):
    '''
        数据库相关操作 
        增删改查
        from app import models 
    '''
    #新增数据
    #models.Usergroup.objects.create(title="销售部")


    #有外键关联的时候 外键代表Usergroup中的一行数据，所以要写ug_id 而不是ug
    #models.Userinfo.objects.create(user='admin',password='password',age='1',ug_id=1)

    #查Usergroup里所有的数据
    #ug_list 是一个对象列表，queryset[obj,obj,obj] 每一个obj封装了自己一行的数据
    #每一个对象代表一行数据,相当于字典，对象.列名 ==值
    #ug_list =models.Usergroup.objects.all() #查Usergroup里所有的数据
    # for i in ug_list:
    #     print(i.id,i.title)

    #查Userinfo里所有的数据
    # models.Userinfo.objects.all()


    # SELECT * FROM usergroup WHERE id =1;
    #若有两个条件，默认用and
    #id__gt=1 表示 id>1 ,id__lt=1 表示id<1
    #group_list =models.Usergroup.objects.filter(id=1) # SELECT * FROM usergroup WHERE id =2;


    #删除
    #models.Usergroup.objects.filter(id=2).delete()

    #更新
    models.Usergroup.objects.filter(id=2).update(title='公关部')

    #获取
    ug_list =models.Usergroup.objects.all()
    return render(request,'orm.html',{'ug_list':ug_list})