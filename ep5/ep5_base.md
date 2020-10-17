今日内容 
    1.CBV FBV

    2.Django ORM
        a.正反向
            增加
                # models.UserType.objects.create(title='普通用户')
                # models.UserType.objects.create(title="特殊用户")
                # models.UserType.objects.create(title='重要用户')
                # models.UserInfo.objects.create(name="nick",age=18,ut_id=1)
                # models.UserInfo.objects.create(name='tom',age=28,ut_id=2)
                # models.UserInfo.objects.create(name='rico',age=18,ut_id=3)
                # models.UserInfo.objects.create(name='jacky',age=20,ut_id=2) 
            单表
                result =models.UserInfo.objects.all()
                    for obj in result:
                print(obj.name,obj.age,obj.ut_id)
            联表
                通过ForeignKey
                多表获取，联表
                obj.ut.title  
                obj.ut.fo.caption
                for obj in result:
                    print(obj.name,obj.ut.title,obj.ut.fo.caption)
            正向查表
                obj.ut代表UserType表中的一行数据
                #带有fk的为正向操作
                obj =models.UserInfo.objects.all().first()
                print(obj.name,obj.age,obj.ut.title)
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

            

        b.数据类型
            .first()    ->#obj
            .all()      ->#[obj obj]
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
                



    3.分页 
        分批获取数据
        #数据库通过切片分批
        models.UserInfo.objects.all()[0:10]
        models.UserInfo.objects.all()[10:20]

        -django自带分页功能

            current_page =request.GET.get('page')
            user_list =models.UserInfo.objects.all()
            paginator =Paginator(user_list,10) 
            try:
                posts =paginator.page(current_page)
            except PageNotAnInteger as e:
                posts =paginator.page(1)
            except EmptyPage as e:
                posts =paginator.page(1)
            return render(request,'index.html',{'posts':posts})

            
            pageinator 含有的功能
            per_page 每页显示的条目数量
            count 数据总个数
            num_pages 总页数
            page_range 总页数的索引范围 如(1,10) (1,200)
            page page对象

            #参数接受一个数字，表示显示第几页

            paginator.page() 含有的功能
            has_next 是否有下一页
            next_page_number 下一页页码
            has_previous 是否有上一页
            previous_page_number 上一页页码
            object_list 分页之后的数据列表
            number 当前页
            paginator paginator 对象
         

        -自定义的分页

上节回顾：
    1.CBV、FBV

    2.models数据库操作
     
            class UserType(models.Model):
                title =models.CharField(max_length=32)
                fo =models.ForeignKey('Foo',null=True,on_delete=models.CASCADE)

            class UserInfo(models.Model):
                name =models.CharField(max_length=16)
                age =models.IntegerField()
                ut =models.ForeignKey('UserType',null=True,on_delete=models.CASCADE)

            class Foo(models.Model):
                caption =models.CharField(max_length=16)

        -跨表
            正向跨表
                1.models.UserInfo.objects.all() -> queryset[obj,obj]
                    q =models.UserInfo.objects.all().first() -> obj
                    q.ug.title -> 取的时候跨表

                2.models.UserInfo.objects.values('nid','ug_id','ug__title')  -> [dict,dict] 查的时候跨表

                3.models.UserInfo.objects.values_list('nid','ug_id','ug__title') ->[tuple,tuple] 查的时候跨表
            反向跨表
                1.q =models.UserGroup.objects.all().first() ->obj
                    q.userinfo_set.all() ->queryset[obj.obj] --obj为userinfo的对象

                2.q =UserGroup.objects.values('id','title','userinfo')
                    .values进行跨表时，使用小写的表明即可，没有set！！
                    q =UserGroup.objects.values('id','title','小写的表名') --默认只取id
                    q =UserGroup.objects.values('id','title','小写的表名__列名') --可以取指定的列名

                3.q =UserGroup.objects.values_list('id','title','userinfo')
                    .values_list进行跨表时，使用小写的表明即可，没有set！！
                    q =UserGroup.objects.values_list('id','title','小写的表名') --默认只取id
                    q =UserGroup.objects.values_list('id','title','小写的表名__列名') --可以取指定的列名
                
        -操作
            UserInfo.objects.all()
            UserInfo.objects.filter(id=1.id=2) 默认为and
            UserInfo.objects.all().first()
            UserInfo.objects.all().count()
            UserInfo.objects.all().update()
            UserInfo.objects.all().delete()
            UserInfo.objects.all()[n:n1] 切片
            跨表：
                正向：
                    xxx.filter('ut__title'=='超级用户').values('id','name','ut__title')
                反向：
                    xxx.filter('表名小写__title'=='超级用户').values('id','name','ut__title')

        








    3.分页组件
        -内置
        -自定义

今日任务：
    1.django orm models操作
        -增删改查
        -其他：
            排序
        
                #正向按照id排序，order_by("id") 反向按照id排序 order_by("-id")
                #若id重复了，则按照name排序
                #obj =models.UserInfo.objects.all().order_by('-id','name')

            分组
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

            基本操作
                models.UserInfo.objects.filter(id__gt =1) #id>1
                models.UserInfo.objects.filter(id__lt =1) #id<1
                models.UserInfo.objects.filter(id__lte=1) #id<=1
                models.Userinfo.objects.filter(id__gte=1) #id>=1
                models.UserInfo.objects.filter(id__in=[1,2,3]) #id在[1,2,3]中
                models.UserInfo.objects.filter(id__range=[1,3]) #bewtwen and
                models.UserInfo.objects.filter(name__startswith='')
                models.UserInfo.objects.filter(name__endswith='')
                models.UserInfo.objects.filter(name__contains='')
                models.UserInfo.objects.filter(id=1) #id=1
                models.UserInfo.objects.exclude(id=1) #id!=1
            
            Q F extra
                -F 更新时取到原来的值
                    from django.db.models import F
                    models.UserInfo.objects.all().update(age=F("age")+1)
                -Q 用于构造复杂的查询条件
                    应用一
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
                    应用二
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


            extra 是对额外的查询条件以及相关表，排序
                models.Userinfo.objects.extra(self,select=none,where=none,params=none,tables=none,order_by=none,select_params=none)
                #a.映射
                    #select selecr_params       -> select 此处 from
                    models.UserInfo.objects.all().extra(select={'n':'select count(1) from app_usertype'})
                    ->select
                        id,
                        name,
                        (select count(1) from tb) as n
                        from xb

                #b.条件
                    #where  params              ->select * from table where 此处
                    models.UserInfo.objects.extra(
                        where=['id=1 or id=2','name=%s'], #(id=1 or id=2)and name=alex
                        params=['alex',]
                    )
                    ->select * from app_userinfo where (id=1 or id=2) and name='alex'   

                #c.表
                    #tables select *            ->from table，此处   
                    models.UserInfo.objects.extra(
                        tables=['app_usertype'],
                        where=['app_usertype.id =app_userinfo.ut_id']
                    )
                    ->select * from app_userinfo,app_usertype where app_usertype.id =app_userinfo.id

                #d.排序
                    #order_by                   ->select * from table order by 此处

                all:
                    models.UserInfo.objects.extra(
                        select={'newid':'select count(1) from app_usertype where id>%s},
                        select_params=[1,],
                        where =['age>%s'],
                        params=[18,]
                        order_by=['-age']
                        tables=['app_usertype']
                    )
                    ->  select 
                        app_userinfo.id,(select count(1) from app_usertype where id>1) as newid
                        from app_userinfo,app_usertype
                        where app_userinfo.age >18
                        orderby app_userinfo.age desc 

                对于很复杂的sql语句依然直接使用sql语句

            原生sql语句
                from django.db import connection,connections

                1.cursor =connection,cursor() == cursor =connections['default'].cursor()

                2.cursor =connections['default'].cursor() #因为django支持多种数据库，第二种方法可选择数据库，default 对应的是setting文件中DATABASE配置中的default

                接下来与pymysql一模一样
                    cursor.execute(原生sql语句)
                    cursor.fetchall()
                    
                

            9.简单的操作
                数据源
                    models.UserInfo.objects.values('nid').distinct()
                    SELECT DISTINCT nid from app_userinfo
                PostgreSQL/MYSQL/SQL
                    models.UserInfo.objects.distinct('nid')
                    SELECT DISTINCT nid from app_userinfo
                反向查表
                    v =models.UserInfo.objects.all().order_by('-id','name') 
                    -> select * from app_userinfo orderby id DESC,name
                
                    v =models.UserInfo.objects.all().order_by('-id','name').reverse()
                    -> select * from app_userinfo order by id,name DESC

                only与defer与using
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
                
                日期处理
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


                聚合不分组
                    #aggregate 也是聚合但是不分组
                    #先对ut_id列去重，在计算ut_id的数量
                    #v =models.UserInfo.objects.aggregate(k=Count('ut_id',distinct=True),n=Count('id')) 
                    #v -> 字典
                
                get
                    #models.UserInfo.objects.get() -> models.UserInfo.object.all().first()
                    #不建议用get 会报错
                
                创建
                    #v =models.UserType.objects.create(title='xxx') ==  v=models.UserType.objects.create(**{'title':'xxx'})
                    #v 为新增数据
                    #obj =models.UserType(title='xxx')
                    #obj.save()
                    #相当于models.UserType.objects.create(title='xxx')

                批量创建
                    # objs =[
                    #     models.UserInfo(name='r11'),
                    #     models.UserInfo(name='r12'),
                    # ]
                    # models.UserInfo.objects.bulk_create(objs,10)  #10代表每提交10个对象commit一次
                
                如果有则获取，若没有则创建
                    #先到表里进行查询roo1，defaults表示要添加的东西
                    #若获取到，obj为对象
                    #查询条件可以添加
                    #created 为布尔值 表示是否增加了
                    #obj,created =models.UserInfo.objects.get_or_create(username='root1',defaults={'email':'111111','u_id':2,'t_id':2})

                若存在就更新，否则创建
                    #obj,created =models.UserInfo.objects.update_or_create(username='root1',defaults={'email':'111111','u_id':2,'t_id':2})

                主键查询
                    #models.UserInfo.objects.in_bulk([1,2,3]) == models.UserInfo.objects.filter(id__in=[1,2,3])
                
                原生sql
                    #extra()
                    #v =models.UserInfo.objects.raw('原生sql')
                    #v ->[obj,obj,obj] obj为userinfo的对象


                在第一次查询时主动做联表
                    # q =models.UserInfo.objects.all().select_related('gt','ut')
                    # #->SELECT * from userinfo inner join usertype on ...
                    # for row in q:
                    #     print(row.name,row.gt.caption,row.ut.titile)

                不做联表，做多次查询
                    #prefetch_related 
                    #q =models.UserInfo.objects.all().prefetch_related('ut')
                    #select * from userinfo ->结果集
                    #django内部把所有的 ut_id =[2,4]
                    #select * from usertype where id in [2,4] ->结果集
                    # for row in q :
                    #     print(row.id,row.ut.title)

                #上述俩个操作比普通跨表效率高
                #有外键 当数据表的数据量少，则用主动联表，select_related
                #数据量多，查询频繁 用prefetch_related

                多对多

                    建表
                    class Boy(models.Model):
                        name =models.CharField(max_length=32)
                        m =models.ManyToManyField('Girl',through="love",through_fields=('b','g')) #也可以写在Girl表中，并且不会往boy里添加任何列，会新建一个表表名为app_boy_m
                        #会新建一个表表名为app_boy_m,表明里有三个列，id，boy_id,girl_id
                        #无法直接对第三张表进行操作，间接对m操作
                        #若自定义了love表l，又保留了ManyToMany，则django会建立四张表，boy girl love 以及app_boy_m
                        #为了避免上述情况发生，给ManyTomany方法加入一个through告诉django 通过自定义的love来创建第三张表
                        #through 通过love来联，throungh_fields 通过b和g来做关联列
    

                    class Girl(models.Model):
                        name =models.CharField(max_length=32)
                        #m =models.ManyToManyField('Boy')

                    class love(models.Model):  #->>此表可以自动生成
                        b =models.ForeignKey('Boy',on_delete=models.CASCADE)
                        g =models.ForeignKey('Girl',on_delete=models.CASCADE)

                        class Meta: #联合索引
                            unique_together=[
                                ('b','g')
                            ]

                    -第一种
                    和leo有关系的姑娘
                        # obj =models.Boy.objects.filter(name="leo").first()
                        # print(obj.name)
                        # love_list =obj.love_set.all()
                        # print(love_list)
                        # for row in love_list:
                        #     print(row.g.name)
                    第二种
                        # lovelist =models.love.objects.filter(b__name='leo')
                        # for row in lovelist:
                        #     print(row.g.name)
                    第3三种 ->好方法
                        # lovelist =models.love.objects.filter(b__name='leo').values('g__name')
                        # for row in lovelist:
                        #     print(row['g__name'])
                    第四种 ->好方法
                        # lovelist =models.love.objects.filter(b__name="leo").select_related('g')
                        # for obj in lovelist:
                        #     print(obj.g.name)

                    ManyToManyField
                        增加
                            #obj =models.Boy.objects.filter(name='leo').first()
                            #obj.m.add(3) #会在app_boy_m里添加 id=1 boy_id =2 girl_id =3 也就是说leo的id为boy_id  3添加到了girl_iod
                            #obj.m.add(2,4)#会在app_boy_m里添加两行数据 boy_id =2 girl_id =2 也就是说leo的id为boy_id  2添加到了girl_iod，还有一行boy_id =2 girl_id =4
                            #obj.m.add(*[1,])#会在app_boy_m里添加一行数据 boy_id =2 girl_id =1

                        删除
                            #obj.m.remove(1)#会在app_boy_m里删除一行数据 删除的是boy_id =2 girl_id =1的数据
                            #obj.m.remove(2,3)#会在app_boy_m里删除2行数据 删除的是boy_id =2 girl_id =2的数据与boy_id =2 girl_id =3的数据
                            #obj.m.remove(*[4,])#会在app_boy_m里添加一行数据 boy_id =2 girl_id 

                        更新
                            #obj.m.set([1,]) #重置

                        获取
                            # tom =models.Boy.objects.filter(name='tom').first()
                            # leo =models.Boy.objects.filter(name='leo').first() #获取leo的对象
                            # # leo.m.add(2)
                            # # tom.m.add(3,4)
                            # # tom =obj.m.all() #->queryset gril 表的obj 获取leo对应的girl的对象
                            # q =leo.m.all().filter(name='kesha').first() #filter里只能填gril表的东西，因为,all() 获取的是gril对象
                            # print(q.name)

                        删除
                            # tom =models.Boy.objects.filter(name='tom').first()
                            # leo =models.Boy.objects.filter(name='leo').first() #获取leo的对象
                            # leo.m.clear() #删除与leo有关的gril

                        反向操作
                            # kesha =models.Girl.objects.filter(name='kesha').first()
                            # # print(kesha.id,kesha.name)
                            # m =kesha.boy_set.all().first() #拿到boy的对象
                            # print(m.name)
                            #注意ManyToManyField的表只能有三列数据！！！！id boy_id gril_id

                        #ManyToManyField与love同时存在时
                        #只可以进行查询以及clear操作，拿到的依然GRIL对象
                    

                    

    2.xss攻击
        -前端慎用safe与mark_safe
        -用的时候需要在渲染前过滤关键字
        
    3.CSRF跨站请求伪造
        -若setting设置中开启了csrf_token 则要在前端表单中加上csrf_token {% csrf_token %}
        -在cookie中也添加了csrf_token
        -本质为随机字符串
        -禁用
            -fbv
                全站禁用
                    -在setting中注释掉csrf表示整个网站都不做csrf验证了
                部分禁用
                    -引入from django.views.decorators.csrf import csrf_exempt 
                    -在url对应的视图函数上添加csrf_exempt装饰器，@csrf_exempt 表示此网页不再验证csrf
                局部应用
                    -先在setting中注释掉csrf，全站禁用
                    -引入from django.views.decorators.csrf import csrf_protect
                    -在url对应的视图函数上添加csrf_protect装饰器，@csrf_protect 表示此网页验证csrf
            -特殊的cbv
                from django.views import View
                from django.views.decorators.csrf import csrf_protect
                from django.utils.decorators import method_decorator

                @method_decorator(csrf_protect,name="post")
                class foo():

                    def dispatch(self,request,*args,**kwargs):
                        obj =super(foo,self).dispatch(request,*args,**kwargs)
                        return obj 
        
                    def get(self,request):
                        pass
                    
                    def post(self,request):
                        pass

            cbv使用的时候,局部验证csrf，需要以下步骤
                -from django.views import View
                -from django.views.decorators.csrf import csrf_protect
                -from django.utils.decorators import method_decorator
                之后在类上面使用 @method_decorator(csrf_protect) 才可以，不可在类中的函数添加，也不可直接@csrf_protect
                    -并可用name参数指定装饰器装饰的方法，@method_decorator(csrf_protect,name="post")，只装饰foo中post方法
                    -若name="dispatch" 则相当于给所有方法都加上csrf_protect装饰器

        -ajex请求
            -第一种方法，从form表单里取csrf_token的值，在提交的formdata中携带
                -先在form表单中放下{% csrf_token %}
                <script src="/static/jquery.js"></script>
                function lean_csrf1() {
                    csrf1 = $('input[name="csrfmiddlewaretoken"]').val()
                    var user = $('#user').val()
                    $.ajax({
                        url: '/csrf1/',
                        type: 'POST',
                        data: {
                            'user': user,
                            'csrfmiddlewaretoken': csrf1,
                        },
                        success: function (data) {
                            console.log(data)
                        }
                    })
                }
            -第二种方法
                使用$.cookie 需要引入jquery.cookie.js，并且依赖jquery.js
                <scrip src="/static/jquery.js"></scrip>
                <scrip src="/static/jquery.cookie.js"></scrip>
                function lean_csrf2() {
                    //从cookie获取csrf_token
                    //document.cookie只能拿到cookie的字符串，需要分割成字典
                    //example    "csrftoken=Yzgn4VqxlKhXLUou81ThoeIABAPLFgEX4CUB5luRGvKMws4vOG9CvMx61AeHOW0I"
                    //使用jqurycookie帮我们自己的分割cookie 使用$.cookie 需要引入jquery.cookie.js，并且依赖jquery.js
                    var csrf1 = $.cookie('csrftoken') //从cookie中获取,从cookie获取的再提交必须放到headers中不能放到formdata里
                    var user = $('#user').val()
                    $.ajax({
                        url: '/csrf1/',
                        type: 'POST',
                        headers: {
                            'X-CSRFToken': csrf1, //在请求中添加从cookie拿的值,并且对于csrf值来说他的key的名字是固定的也是django要求的必须为X-CSRFToken
                        },
                        data: {
                            'user': user,
                        },
                        success: function (data) {
                            console.log(data)
                        }
                    })
                }

                        
        
    4.模板引擎
        部分方法
        自定义方法

上节回顾
    -数据库的操作
        -models.TABLE.objects.create(title="xx")
        -filter(id=1,name='ff')
        -filter(id=1,name='ff').update()
        -filter(id=1,name='ff').delete()
        -.all()
        -.values() ->[{},{},{}]
        -.count()
        -values_list() ->[(),(),()]
        -values_list() #小写的表名__
        -bulk_create(obj_list,commit的数据量)
        -q =models.xx.objects.all().only('id') ->[obj,obj]
        -F,更新数据
        -Q，做and或者or，加到filter做条件
        -filter()与annotate
        -order_by().reverse()
        -extra
            -select={x:'1'} select 1 as x from TABLE
            -params
            -select_params
            -tables=['x',]
            -where
            -order_by
        -filter(id__range=[1,3])
        -exclude
        -existe
        -annotate 与 values 做group by
        -.raw()
        -aggregate 聚合整张表
        -filter(id__gt)
        -filter(id__lt)
        -filter(id__gte)
        -filter(id__lte)
        -filter(id__in=[x,n])
        .first()
        .get()
        -last()
        -only()
        -defer()
        -connection 或者 connections
        -max() min() sum() avg() 聚合
        -makemigrations
        -migrate
        -reverse()
        -destinct()
        -dates 日期处理
        -get_or_create
        -update_or_create
        -filter(age__isnull=True)
        -using

        #若表内容多，推荐使用字典的方式
            create(name='xx',age='xx')
            dict={"name":"xx","age":"xx"}
            create(**dict)

        #更新
            models.xx.objects.filter(id=1).update(a=1,b=2)
            models.xx.objects.filter(id=1).update(**dic)

        #查询
            models.xx.objects.filter(id=1,xxx)
            models.xx.objects.filter(**dict)
        
        FORM 组件可以实现
            -django 把数据转换成字典 
            -对用户发来的数据进行验证
            

上节回顾

        


    -xss攻击
    
