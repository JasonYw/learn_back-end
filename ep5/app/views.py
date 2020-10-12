from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views import View
from app import models
from django.core.paginator import Paginator,Page,PageNotAnInteger,EmptyPage
    
 

# Create your views here.
def test(request):
    '''
        get 查
        post 创建
        delete 删除
        put 更新 
        html里 form表单 只有get和post
        ajax里 有其他的方式
    '''
    '''
        增加
    '''
    # models.UserType.objects.create(title='普通用户')
    # models.UserType.objects.create(title="特殊用户")
    # models.UserType.objects.create(title='重要用户')
    # models.UserInfo.objects.create(name="nick",age=18,ut_id=1)
    # models.UserInfo.objects.create(name='tom',age=28,ut_id=2)
    # models.UserInfo.objects.create(name='rico',age=18,ut_id=3)
    # models.UserInfo.objects.create(name='jacky',age=20,ut_id=2) 
    '''
        单表获取
    
    result =models.UserInfo.objects.all()
    for obj in result:
        print(obj.name,obj.age,obj.ut_id)
    '''


    print('------------------------------------')


    '''
        通过ForeignKey
        多表获取，联表
        obj.ut.title  
        obj.ut.fo.caption
    
    for obj in result:
        print(obj.name,obj.ut.title,obj.ut.fo.caption)
    '''


    print('------------------------------------')


    '''
        obj.ut代表UserType表中的一行数据
    #带有fk的为正向操作
    obj =models.UserInfo.objects.all().first()
    print(obj.name,obj.age,obj.ut.title)
    '''


    print('------------------------------------')


    '''
    反向关联
    #UserType,表名小写 usertype_set.all() -- 反向操作
    obj =models.UserType.objects.all().first()
    obj.userinfo_set.all() #拿到queryset
    #usertype的obj第一个值为id=1 普通用户
    #而obj.userinfo_set.all()拿到的是对应的userinfo表中ut_id=1的行的对象
    print(obj.id,obj.title,obj.userinfo_set.all())  
    for obj in obj.userinfo_set.all():
        #obj为userinfo对象
        print(obj.name,obj.age)

    #若item.userinfo_set.filter()是对userinfo那个表做筛选
    #filter里面的参数是用户表的列名
    result =models.UserType.objects.all()
    for item in result:
        print(item.title,item.userinfo_set.filter())
    '''

    print('------------------------------------')

    '''
    #obj
    #[obj obj]
    #只取id与name列，result依然是queryset类型，但是里面变成字典
    #.all().values() 拿的是字典类型
    result =models.UserInfo.objects.all().values('id','name')
    for row in result:
        print(result)
    #.all().values_list()拿的是元组
    #.all() queryset类型里面是对象
    result =models.UserInfo.objects.all().values_list('id','name')
    for row in result:
        print(result)

    #数据库获取多个数据时
    #可以跨表，封装很多值
    1.[obj,obj]
    models.UserInfo.objects.all()
    models.UserInfo.objects.filter()

    2.[{id:1,name:xx},{id:2,name:yy},{id:3,name:oo}]
    #这种方式无法跨表，但是取值的时候进行一些操作即可跨表
    models.UserInfo.objects.all().values('id','name')
    models.UserInfo.objects.filter(id_get=1).values('id','name')

    2__
    models.UserInfo.objects.all().values('id','name'，'ut__title')
    models.UserInfo.objects.filter(id_get=1).values('id','name','ut__title')


    3.[(1,xx),(2,yy),(3,oo)]
    #这种方式无法跨表,但是取值的时候进行一些操作即可跨表
    models.UserInfo.objects.all().values_list('id','name')
    models.UserInfo.objects.filter(id_get=1).values_list('id','name')

    3__
    models.UserInfo.objects.all().values_list('id','name','ut__title')
    models.UserInfo.objects.filter(id_get=1).values_list('id','name','ut__title')

    1在循环的时候进行跨表
    2，3在查的时候进行跨表
    '''

    result =models.UserInfo.objects.all().values('id','name','ut__title')
    for item in result:
        print(item)
   
    return HttpResponse('....')


class login(View): 
    '''
        from django.views import View
        需要继承
        优先执行 dispach 本质是getattr
        getattr() 函数用于返回一个对象属性值。
        所以可以做成装饰器
    '''

    def dispatch(self,request,*args,**kwargs):
        print('before')
        obj =super(login,self).dispatch(request,*args,**kwargs)
        print('after')
        return obj 

    def get(self,request):
        return render(request,'login.html')
 
    def post(self,request):
        print(request.POST.get('user'))  
        return HttpResponse('Login.post')
    
    

def index(request):
    '''
    分页
    '''
    current_page =request.GET.get('page')
    user_list =models.UserInfo.objects.all()
    paginator =Paginator(user_list,10) 
    '''
        pageinator 含有的功能
        per_page 每页显示的条目数量
        count 数据总个数
        num_pages 总页数
        page_range 总页数的索引范围 如(1,10) (1,200)
        page page对象
    '''


    #参数接受一个数字，表示显示第几页
    try:
        posts =paginator.page(current_page)
    except PageNotAnInteger as e:
        posts =paginator.page(1)
    except EmptyPage as e:
        posts =paginator.page(1)
    '''
    has_next 是否有下一页
    next_page_number 下一页页码
    has_previous 是否有上一页
    previous_page_number 上一页页码
    object_list 分页之后的数据列表
    number 当前页
    paginator paginator 对象
    '''

    return render(request,'index.html',{'posts':posts})
