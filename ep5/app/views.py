from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views import View
from app import models
 

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
    print('------------------------------------')
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
    '''

         




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
    
     