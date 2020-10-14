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


    

    
    2.xss攻击

    3.CSRF跨站请求伪造

    4.模板引擎
        部分方法
        自定义方法

    
