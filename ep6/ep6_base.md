上节回顾

    数据库操作：
        -app
            -models.py
                class foo(models.Model):
                    字段类型：
                        字符串类：
                            username =models.CharField()
                        时间类：
                            models.DateTimeField() 这个mysql里也支持时间格式，所以我们可以直接用
                        数字类：
                            integer =models.IntegerField()
                            floater =models.FloatField()
                            Decimaler =models.DecimalField(max_digits=30,decimal_places=10)#max_digit设置总长度，decimal_places设置小数的位数
                        枚举类(django的枚举类于mysql有区别)：
                            color_list =(
                                (1,'black'),
                                (2,'white'),
                                (3,'blue'),
                            )
                            color =models.IntegerField(choices=color_list) 
                            #color_list会存在内存中
                            #choices 代表可选择的 也就是这个列只有1，2，3能填入
                            #不一定为IntegerField，也可以为CharField
                            #但是一般为IntegerField
                            1.自己操作
                                自己取，自己用
                            2.给django-admin用
                                会做成下拉框，框里的option为黑色白色蓝色
                            应用场景
                                选项固定不变
                                #为啥不单弄一张表做一个外键约束
                                    -外键约束涉及到联表，性能差
                                    -元组不可以动态增加，所以选项永远不变的，可以不建外键约束
                                选项为动态的
                                    就要用外键约束ForeignKey
                    字段参数：
                        -针对数据库的参数
                            email =models.EmailField(null=True,default='1111',unique=True)
                            #unique为唯一索引，default为默认值，值可以为空
                            integer =models.IntegerField(null=True,db_index=True,primary_key=True)
                            #db_idnex为索引,primary_key设置主键
                            联合索引
                                class Meta: 
                                    # unique_together=(#联合唯一索引
                                    #     ('email','c-time'),
                                    # )
                                    index_together=(#联合不唯一索引
                                        ('email','c-time'),
                                    )
                            1.null=True,
                            2.default='1111',
                            3.unique=True
                            4.db_index=True,
                            5.primary_key=True
                            6.max_length=12
                            7.class Meta: 
                                unique_together =(()),
                                index_together=(())
                            8.choices
                    
                    -针对django-admin的特殊类：
                        email =models.EmailField()
                        ip =models.IPAddressField()
                        slug =models.SlugField()
                        uuid =models.UUIDField()
                        filepath =models.FilePathField()
                        file =models.FieldFile()
                        image =models.ImageField()
                        以上本质上都是字符串
                        a.直接通过
                            models.Userinfo.objects.create() 将不会影响 也就是都是字符串
                            -- ModelForm
                        b.影响django自带的管理工具admin

                    -针对django-admin的参数
                        floater =models.FloatField(null=True,blank=True,verbose_name="age",editable=True,help_text='help you')
                        #以下针对django-admin而言 
                        #blank 是否可以为空ch
                        #editable 是否可以编辑
                        #verbose_name 在django-admin中的input中改名字
                        #help_text 输入框的提示信息
                        #error_messages 自定义错误信息，但是优先级较低，django-admin不会优先显示它

        -操作：
            -增删改查
            -filter(),update(),create() 可以加字典 **dict
            -all() values() values_list()
            -FK
                正向：
                    filter() values() values_list() -> fk__xx
                    objs =all()
                    for obj in objs:
                        obj.fk.
                反向:
                    
                    filter() values() values_list() -> 表名称__xx
                    objs =all()
                    for obj in objs:
                        obj.表明_set.all()
            -ManytoMany
                -自定义
                -manytomany
                    正向
                        有m2m的为正向
                        obj =...
                        obj,m.add()
                        obj.m.remove()
                        obj.m.set()
                        obj.m.clear()
                        obj.m.all()
                    反向
                        obj ....
                        obj.表名_set.add()
                        obj.表名_set.remove()
                        obj.表名_set.set()
                        obj.表名_set.clear()
                        obj.表名_set.all()
                -自定义+manytomany
                    obj =...
                    obj.m.clear()
                    obj,m.all()
                 





    csrf：
        post的时,需要用户携带随机字符串csrf_tocken
        -form表单携带{% csrf_tocken %}
        -ajex
            -从form里取放在ajex中的formdata中
            -利用$.cookie从cookie中取csrf_token，放在headers中
    xss：
        -不要用safe
        -在后台使用mark_safe
        -过滤关键字
    cookie：
        -保存在客户端浏览器中的键值对
        -放在用户浏览器端的键值对
        -可以放很多，对于敏感信息不能放在cookie中


    