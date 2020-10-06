1.http://127.0.0.1:8000/index/?nid=xxx 
    path('edit/', views.edit),
    views
    def edit(request):
        request.GET.get('nid')
        return HttpResponse('....')
        -这种方式不好 
        -seo 百度游览器收录权重较低
        -因为get传参 url中的参数会经常变化
http://127.0.0.1:8000/index/xxx/ 
    re_path(r'edit/(\w+).html/',views.edit),
        -.html伪静态
    views
    def edit(request,a1):
        a1参数代表正则表达式的内容
        return HttpResponse('....')
        -这种比较好 url传参会降低seo的优先值


今日内容：
    django-admin startproject mysite
    cd mysite
    python manage.py startapp app(自定义)
    django 里面可有多个app
    因为一个主站 一个后台管理
    不同业务为一个app
    app
        -migrations 数据库相关
        -admin django提供的后台管理 数据库相关
        -models 写类 根据类创建数据库表 
        -tests  做单元测试
        -views 视图
    1.路由系统
        url->函数

        a.path('admin/', views.login), - def login(request)
        b.re_path(r'edit/(\w+)/(\w+)/',views.edit) -> def add_user(request,a1,a2)
            -加正则表达式（可加多个正则表达式）
            -多几个正则 就要在路由函数中加几个参数 动态路由 需用re_path，
            -在视图函数 加一个参数a1。。。an 接受正则表达式的内容,除request 参数数量为正则表达式的数量，并且顺序也是匹配的
        c.re_path(r'edit/(?P<a>\w+)/',views.edit) -> def add_user(request,a1)
            ps:
                -终止符：
                    re_path(r'edit$',views.edit) def add_user(request)
                -伪静态
                    re_path(r'edit/(\w+).html$',views.edit) -> def add_user(request,a1)

        d.路由分发
            -urls.py
                -引入from django.urls import path,include
                path('app/',include('app.urls')), 
            -app.urls.py
                re_path(r'index.html$',views.index)
            -app01.urls.py
                re_path(r'index.html$',views.index)

            项目目录中的urls文件 path('app/',include('app.urls')), 
            app以及app01中的urls文件 re_path(r'index.html$',views.index)
            http://127.0.0.1:8000/app/index.html -> 先去app中匹配urls文件中的地址 对应的views
            http://127.0.0.1:8000/app01/index.html ->先去app01中匹配urls文件中的地址 对应的views
            项目目录中的urls文件 path('',views.default) ->定义错误页面

        e.给url关系命名
            re_path(r'index/(?P<a1>\d+)',views.index,name="n1")
            根据n1可反生成url
                -  先导入from django.urls import reverse
                def index(request,a1):
                    reverse('n1',kwargs={'a1':111}) 生成/index/111
            
            path('index/',views.index,name="n1")
            reverse('n1') 生成/index/

            re_path(r'index/(\d+)',views.index,name="n1")
            reverse('n1',args=(1,)) 生成index/1

    2 ORM操作

        步骤：
            -创建数据库
            -setting配置
              DATABASES ={
                    'default':{
                        'ENGINE':'django.db.backends.mysql', #写死的
                        'NAME':'django', #DATABASE的名字
                        'USER':'root',
                        'PASSWORD':'0125',
                        'HOST':'localhost',
                        'PORT':'3306',
                    }
                }
            -与setting同目录中的__init__
                import pymysql
                pymysql.install_as_MySQLdb()

            -在app中的models文件中创建一个类，类要继承models.Model相当于创建一个表
                class Userinfo(models.Model):
                    '''
                        创建一行表
                    '''
                    #自增int
                    #nid =models.AutoField()

                    #自增长整型 primary_key=True设置主键
                    #可以不写 django会自动创建一列名为id的主键 int 自增 主键 
                    id =models.BigAutoField(primary_key=True)  

                    #字符串类型 max_length最大长度为32 CharField必须指定max_length
                    user=models.CharField(max_length=32)

                    #字符串类型 max_length最大长度64
                    password =models.CharField(max_length=64)

                    #给旧数据库的时候，添加新列的时候
                    # 要说明null=True ，也就是可以为空 或 default=1 添加默认值
                    age =models.IntegerField(default=1) 

                    #添加外键约束，但是要允许空值,在数据库里会生成 ug_id 存的是外键的id
                    ug =models.ForeignKey('Usergroup',null=True,on_delete=models.CASCADE)


                class Usergroup(models.Model):
                    title =models.CharField(max_length=32)

                
            -去setting里面注册app
                在setting中的INSTALLED_APPS中加上app文件夹的名字
                INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'app'
                ]

            -创建数据库表，创建于修改都是这两个命令
                -命令：
                    python manage.py makemigrations
                    python manage.py migrate

                每一次执行命令 会读取注册过的app中的类 并在app中的migrations中创建新的配置文件
                并且migrations中的配置文件会记录所有表的创建及修改记录
                

    


            


        HTTP请求：
            url -> 视图（模板+数据）

        ORM操作表
            -创建表
            -修改表
            -删除表

        ORM操作数据行
            -增删改查

        ORM：没办法直接连接数据库
        默认：mysql -> mysqlDB（python3中没有)
            所以要修改django默认连接mysql的方式
            利用pymysql第三方工具连接数据库
            django默认会连接sqllite 
            所以要在setting中设置


        setting:
                DATABASES ={
                    'default':{
                        'ENGINE':'django.db.backends.mysql', #写死的
                        'NAME':'django', #DATABASE的名字
                        'USER':'root',
                        'PASSWORD':'0125',
                        'HOST':'localhost',
                        'PORT':'3306',
                    }
                }

        __init__:
            import pymysql
            pymysql.install_as_MySQLdb()


作业：
    学员管理（sql换成orm）
        新url方式：
            1.班级的增删改查
                -传参要用正则表达式
                /edit-class?nide=1 换成 /edit-class/1.html
            2.学生管理（涉及到链表，正向反向操作）
                神奇的双下划线


今日内容 CBV FBV 
    1.CBV FBV
    2.Django ORM
    3.分页 
        -django自带分页功能
        -自定义的分页
