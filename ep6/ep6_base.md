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
                 -补充关联
                    class UserInfo(models.Model):
                        nickname =models.CharField(max_length=32)
                        username =models.CharField(max_length=32)
                        password =models.CharField(max_length=64)
                        gener_choices =(
                            (1,'boy'),
                            (2,'girl')
                        )
                        gender =models.IntegerField(choices=gener_choices)

                    class btoy(models.Model):
                        '''
                        g与b不能一样
                        related_query_name 代表当需要反向查表时，related_query_name的值代表表名
                        也就是当女生反向查表 a_set.all()
                        男生：b_set.all()
                        related_name 代表当需要反向查表时 related_name 的值代表表名
                        而且不要_set了，直接是a.all() b.all()
                        '''
                        g =models.ForeignKey(to='UserInfo',related_name='g',on_delete=models.CASCADE)
                        b =models.ForeignKey(to='UserInfo',related_name='b',on_delete=models.CASCADE)
                                
                #男生对象
                obj =models.Userinfo.objects.filter(id=1).first()
                #根据男生id=1查找关联的所有的女生
                obj.b.all() #拿到此男生与女生有关系的关系表
                for i in obj.b.all()：
                    i.g.nickname 通过联表拿到女生的信息
            -自关联
                class Comment(models.Model):
                    news_id =models.IntegerField()
                    content =models.CharField(max_length=32)
                    user =models.CharField(max_length=32)
                    '''
                        关联自己的id，因为replayid只能是id存在的值
                    '''
                    replyid =models.ForeignKey('Comment',null=True,blank=True,related_name='replyid')


                    '''
                        新闻id  内容 用户   reply_id
                    1    1      hh   root    null
                    2    1      hh   root    null
                    3    1      xx   shaowei null
                    4    2      cc   root    null 
                    5    1      nn   llll     2
                    6    1      zz   xxxx     2
                    7    1      ff   cccc     5
                    '''
                '''
                新闻1    
                    hh
                    hh
                        -nn
                            -ff
                        -zz
                    shaowei
                    root
                新闻2
                    cc
                '''

                
                 








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

今日内容
    模版
        -基本使用
        -母版
            -页面继承
        -导入(include)  {% include "xxxxx.html" %} 把html源码在此位置加载
            小组件与母版功能类似但是不一样，母版是用来继承的
            include是引入过去的
        -母版与导入工作流程，视图函数返回html文件，html先进行继承或者include，之后在渲染模板所以，在小组件中的{{}} 也会被渲染
        -函数->自动执行
        -模版里自定义函数：
            -simpletage
            -注册app
            -在app中建立templatetags文件夹
            -在templatetags中建立任意py文件,比如xx.py
            -在文件中
                from django import template
                register =template.Library() #写死的，变量名也不能变
            -在自定义函数上加@register.filter
                -在html文件中 {% load xx %}
                    当自定义函数只有一个参数时
                        -在使用的地方{{ 参数｜自定义函数名 }}
                    当自定义函数有两个参数时
                        {{ 参数1｜函数名:参数2 }}  冒号后面不能有空格
                    filter最多只支持两个参数
                        若想加多个参数，则只能把其他参数都放在参数2中，之后进行split处理
                    但是filter 可以与if一起用
                    {% if 参数一｜函数:参数二 %}
                        执行语句
                    {% endif %}
            -在自定义函数上加@register.simple_tag
                -对于参数数量无限制
                -{% 函数名 参数 参数 参数 %} 函数名与参数之间必须有空格，参数与参数之间也必须有空格
                -但是不可以与if一起使用
            

    session
        cookie是什么？
            保存在客户端浏览器上的键值对
            浏览器1：cookie --- "asdadasdweasdasda" 
            浏览器2：cookie --- "asddsdsdsDsdsdsds"
        session是什么？
            保存在服务器端的数据（本质是键值对）
            {
                "asdadasdweasdasda":{"id":1,"name":"xx",email='xxx'}
                "asddsdsdsDsdsdsds":{"id":2,"name":"xxx",email='nnn'}
            }
            应用：依赖于cookie
            作用：保持会话(web网站) ，记住登陆状态
            好处：好处敏感信息不会直接给客户
        内部流程：
            浏览器登录成功后，服务器端给浏览器一个随机字符串，服务器端保存这个随机字符串，作为那个浏览器的信息的key，登录信息为value
            浏览器拿到随机字符串存到cookie中。
        梳理：
            1.保存在服务端的数据(本质为键值对)
            2.配置文件
                -存储位置
                -超时时间、每一次刷新是否更新时间
            3.
                request.session
                    -增删改查
                    -获取随机字符串
                    -主动设置超时时间
        
                    
    中间件
        
上节回顾+补充：
    1.django请求的生命周期
        -url -> 视图。。。
        -中间件 ->url->视图。。。
        -web框架的本质：socket
        -django里面没有socket
        -别人的socket+django 遵循wsgi web服务网关接口
            -django默认用的wsgiref+django
            -uwsgi+djagno
            def main():
                sock =socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
                sock.bind(('localhost',8000))
                sock.listen(5)
                while True:
                    client,address =sock.accept()
                    v =client.recv(1024)
                    #自己解析：各种split

                    #请求相关
                    django
                    #产出字符串
                    client.send(产出字符串)
                    client.close()



作业：
    1.相亲管理 
        -用户登录 session
        -装饰器
    2.数据表    
        -男生表，女生表，两个表
            表：
                id 用户名 密码
            关系表
                男id 女id
    3.功能：
        登录页：
            用户名
            密码
            性别 
            checkbox：是否一周免登录，把默认改成一天
            session[id],session[sex]
        查看异性列表：
        查看与自己约会过的列表：



        



    