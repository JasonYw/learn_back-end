from django.core.paginator import EmptyPage, Page, PageNotAnInteger, Paginator
from django.db.models import Count, Max, Min, Sum
from django.shortcuts import HttpResponse, redirect, render
from django.views import View
from utils.pager import PageInfo
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

    print('------------------------------------')
    '''
    正向
    q =models.UserInfo.objects.values("id","name","ut__title")
    相当于select * from userinfo leftjoin usertype
   

    反向
    涉及到联表
    q =models.UserType.objects.values('id','title','userinfo')
    相当于select * from usertype leftjoin userinfo 

    区别：
        leftjoin 是以左为准
        正向：是以userinfo为准
        反向：是以usertype为准
   
    '''
    #排序
    #正向按照id排序，order_by("id") 反向按照id排序 order_by("-id")
    #若id重复了，则按照name排序
    #obj =models.UserInfo.objects.all().order_by('-id','name')

    #分组
    #from django.db.models import Count,Sum,Max,Min
    #.query 生成sql语句
    #annotate 写聚合条件
    #xx为别名
    #v =models.UserInfo.objects.values('ut_id').annotate(xx=Count('id')) 
    #SELECT `app_userinfo`.`ut_id`, COUNT(`app_userinfo`.`id`) AS `xx` FROM `app_userinfo` GROUP BY `app_userinfo`.`ut_id` ORDER BY NULL


    #分组之后2次筛选,filter在annotate相当于sql中的HAVING
    #v =models.UserInfo.objects.values("ut_id").annotate(xx=Count("id")).filter(xx__gt=2)
    #SELECT `app_userinfo`.`ut_id`, COUNT(`app_userinfo`.`id`) AS `xx` FROM `app_userinfo` GROUP BY `app_userinfo`.`ut_id` HAVING COUNT(`app_userinfo`.`id`) > 2 ORDER BY NULL
    #filter在annotate相当于sql中的WHERE
    #v =models.UserInfo.objects.values("ut_id").filter(id__gt =2).annotate(xx=Count("id")).filter(xx__gt=2)
    #SELECT `app_userinfo`.`ut_id`, COUNT(`app_userinfo`.`id`) AS `xx` FROM `app_userinfo` WHERE `app_userinfo`.`id` > 2 GROUP BY `app_userinfo`.`ut_id` HAVING COUNT(`app_userinfo`.`id`) > 2 ORDER BY NULL

    #基本操作
    # models.UserInfo.objects.filter(id__gt =1) #id>1
    # models.UserInfo.objects.filter(id__lt =1) #id<1
    # models.UserInfo.objects.filter(id__lte=1) #id<=1
    # models.Userinfo.objects.filter(id__gte=1) #id>=1
    # models.UserInfo.objects.filter(id__in=[1,2,3]) #id在[1,2,3]中
    # models.UserInfo.objects.filter(id__range=[1,3]) #bewtwen and
    # models.UserInfo.objects.filter(name__startswith='')
    # models.UserInfo.objects.filter(name__endswith='')
    # models.UserInfo.objects.filter(name__contains='')
    # models.UserInfo.objects.filter(id=1) #id=1
    # models.UserInfo.objects.exclude(id=1) #id!=1

    '''
    #F Q EXTRA
    from django.db.models import F
    #F获取原来的值
    models.UserInfo.objects.all().update(age=F("age")+1)

    #Q
    #Q使用有两种方式：对象方式，以方法的方式
    models.UserInfo.objects.filter(id=1,name="root") 
    #等效于
    condition={
        'id':1,
        'name':'root',
    }
    models.UserInfo.objects.filter(**condition)

    from django.db.models import Q
    #等效于
    #一个Q代表一个条件
    #第一种写法
    models.UserInfo.objects.filter(Q(id=1) | Q(name='alex'))
    models.UserInfo.objects.filter(Q(id=1) & Q(name='alex'))

    
    #第二种
    #(c1=1 or c1=10 or c1=9)
    q1 =Q()
    q1.connector ="OR"
    q1.children.append(('c1',1))
    q1.children.append(('c1',10))
    q1.children.append(('c1',9))

    #id=1 or id=2 or id=9 
    q2 =Q()
    q2.connector ="OR"
    q2.children.append(('id',1))
    q2.children.append(('id',2))
    q2.children.append(('id',9))

    #q1 and q2
    con =Q()
    con.add(q1,'AND')
    con.add(q2,'AND')
  

    #id=1 and id=10
    q3 =Q()
    q3.connector ='AND'
    q3.children.append(('id',1))
    q3.children.append(('id',10))

    #q2最后一个元素 or q3,q3在q2内部
    q2.add(q3,'OR') 

    #上述相当于
    (id=1 or id=2 or id=9 or (id=1 and id=10)) and (c1=1 or c1=10 or c1=9)


    #动态生成
    condition_dict ={
        'k1':[1,2,3,4],
        'k2':[1,],
        'k3':[11,]
    }
    con =Q()
    for k,v in condition_dict.items():
        q =Q()
        q.connector ='OR'
        for i in v:
            q.children.add('id',i)
        con.add(q,'AND')

    models.UserInfo.objects.filter(con)
    '''

    print('------------------------------------')

    #extra
    # v =models.UserInfo.objects.all().extra(select={'n':'select count(1) from app_usertype'})
    # v =models.UserInfo.objects.all().extra(
    #     select={
    #         'n':'select count(1) from app_usertype where id =%s and id =%s',
    #         'm':'select count(1) from app_usertype where id =%s',
    #         },
    #         select_params=[1,2,3,])
    #相当于
    # select
    #     id,
    #     name,
    #     (select count(1) from tb) as n
    #     from xb
    #where
    # for obj in v:
    #     print(obj.name,obj.id,obj.n,obj.m)
    # models.UserInfo.objects.extra(
    #     where=['id=1 or id=2','name=%s'], #(id=1 or id=2)and name=alex
    #     params=['alex',]
    # )   
    # models.UserInfo.objects.extra(
    #     tables=['app_usertype'],
    #     where=['app_usertype.id =app_userinfo.ut_id']
    # )
    # # 相当于select * from app_userinfo,app_usertype where app_usertype.id =app_userinfo.id

    v =models.UserInfo.objects.filter(id__gt=1).extra(
        where=['app_userinfo.id<%s'],
        params=[100,],
        tables=['app_usertype'],
        order_by=['-app_userinfo.id'],
        select={'uid':1}
    )
    print(v.query)



    #select ut_id from userinfo
    # result =models.UserInfo.objects.all().values('id','name','ut__title')
    # for item in result:
    #     print(item)

    # v =models.UserInfo.objects.all().order_by('-id','name')
    # print(v)
    # v =models.UserInfo.objects.all().order_by('-id','name').reverse()
    # print(v)
    v =models.UserInfo.objects.all()
    #[obj]
    v =models.UserInfo.objects.all().only('id','name') #能写only尽量写only
    #[obj.id/obj.name]
    models.UserInfo.objects.values('id','name')
    #[id,name]
    v =models.UserInfo.objects.all().defer('name')
    #[obj.age] #拿到除了name以外的数据
    #v =mdoels.UserInfo.objects.all().using('指定的数据库')
    #models.UserInfo.objects.all().filter().all().exclude().only().defer()  


    #year 年-01-01
    #month 年-月-01
    #day:年-月-日
    #models.表.objects.dates('列','day','DESC') 先格式化在排序

    #kind只能是year month day hour minute second
    #tzinfo 时区
    #转换时区
    #需要pytz模块 pip install pytz
    # import pytz
    # pytz.all_timezones
    # pytz.timezone('Asia/Shanghai')
    #models.表.objects.datetimes('列',kind='',tzinfo='Asia/Shanghai') 


    #aggregate 也是聚合但是不分组
    #先对ut_id列去重，在计算ut_id的数量
    #v =models.UserInfo.objects.aggregate(k=Count('ut_id',distinct=True),n=Count('id')) 
    #v -> 字典

    #models.UserInfo.objects.get() -> models.UserInfo.object.all().first()
    #不建议用get 会报错

    #v =models.UserType.objects.create(title='xxx') ==  v=models.UserType.objects.create(**{'title':'xxx'})
    #v 为新增数据
    #obj =models.UserType(title='xxx')
    #obj.save()
    #相当于models.UserType.objects.create(title='xxx')

    #批量创建
    # objs =[
    #     models.UserInfo(name='r11'),
    #     models.UserInfo(name='r12'),
    # ]
    # models.UserInfo.objects.bulk_create(objs,10)  #10代表每提交10个对象commit一次


    #如果有则获取，若没有则创建
    #先到表里进行查询roo1，defaults表示要添加的东西
    #若获取到，obj为对象
    #查询条件可以添加
    #created 为布尔值 表示是否增加了
    #obj,created =models.UserInfo.objects.get_or_create(username='root1',defaults={'email':'111111','u_id':2,'t_id':2})
    #若存在就更新，否则创建
    #obj,created =models.UserInfo.objects.update_or_create(username='root1',defaults={'email':'111111','u_id':2,'t_id':2})

    #主键查询
    #models.UserInfo.objects.in_bulk([1,2,3]) == models.UserInfo.objects.filter(id__in=[1,2,3])

    #原生sql
    #extra()
    #v =models.UserInfo.objects.raw('原生sql')
    #v ->[obj,obj,obj] obj为userinfo的对象



      

    return HttpResponse('200')


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
    # for i in range(300):
    #     models.UserInfo.objects.create(name="name"+str(i),age=18,ut_id="1")
    # return HttpResponse('200')

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


def custom(request):
    #表示用户当前想要访问的页码 8
    current_page =int(request.GET.get('page'))
    #每页显示数据的个数
    per_page =10 

    #总个数
    num_userinfo =models.UserInfo.objects.all().count()
    # num_userinfo =models.UserInfo.objects.filter(id__lt=22).count()

    page_info =PageInfo(current_page,per_page,num_userinfo,11,'/custom.html')
    userlist =models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'custom.html',{'userlist':userlist,'page_info':page_info})

    