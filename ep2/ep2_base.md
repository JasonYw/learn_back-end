1.Django框架
    pip install django
    
    1.新建一个django项目
        -django-admin startproject a
        会在目录下创建一个名为a的django项目
        项目中包含一个文件夹a和一个manage.py
        /：
            -manage.py对网站的所有管理
        a：
            -settings.py存储配置信息
            -urls.py 存储url和函数的对应关系，路由系统
            -wsgi.py 实现socket

    2.在django项目根目录中，启动网站，服务端开始监听ip地址以及端口号
        -python manage.py runserver 127.0.0.1:8080 
        若此命令不给ip地址以及端口号，默认监听127.0.0.1:8000
        若不给端口号，默认监听8000端口
    
2.Django程序目录:

    ep2_django:

        -manage.py #对当前django程序所有操作可以基于python manage.py runserver 加参数即可
        
        -ep2_django:
            -settings.py #django配置文件
            -urls.py #路由系统 urls->函数 的关系
            -wsgi.py #用于定义django用socket，默认wsgiref,uwsgi

3.创建项目固定步骤
    a.创建project -django-admin startproject 
    b.配置：
        在django项目根目录下创建templates文件夹，用来存放html文件，或任意存储字符串的文件
        在django项目根目录下创建temp_css文件夹，用来存储图片或者css样式
        setting.py:
            -模板路径 给render函数用的 TEMPLATES中进行配置
                其中BASE_DIR代表django项目当前路径，templates代表存放render读取文件所存放的文件夹名字
                TEMPLATES = [
                    {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        'DIRS': [os.path.join(BASE_DIR, "templates"),], #此参数决定render读取到的文件的目录 templates为目录名字，此目录要在项目的根目录中
                        'APP_DIRS': True,
                        'OPTIONS': {
                            'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                            ],
                        },
                    },
                ]
            -静态文件路径 给html中css以及图片用的   STATIC_URL 配置前缀 以及STATICFILES_DIRS配置路径
                其中STATICFILES_DIRS是元组所以必须要加逗号！！！
                STATIC_URL = '/static/'
                STATICFILES_DIRS =(
                    os.path.join(BASE_DIR,'temp_css'), #必须要逗号！！！
                )
            -注释掉setting中MIDDLEWARE中'django.middleware.csrf.CsrfViewMiddleware'
                MIDDLEWARE = [
                    'django.middleware.security.SecurityMiddleware',
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                    #'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                ]


    若出现模板无法找不到问题，去setting里找TEMPLATES、STATICFILES_DIRS、STATIC_URL问题，以及目录是否建立在根目录下 

4.url对应关系
    /login/    login

    def login(request): reques代表用户请求的所有数据，请求头+请求体
        request.method  代表请求的类型 post get 或者 put...
        request.GET 代表GET请求中的参数，字典形式
        request.POST 代表POST请求中的FORM DATA表单数据，字典形式

        return HttpResponse(...) 用于给客户端返回字符串
        return render(request,'xxx.html',{....}) 用于给客户端返回HTML源文件，并且可以加渲染
        return redirect('跳转的网址') 用于网页跳转，重定向
    
    备注： 
    -GET请求 request.GET有值 request.POST无值 
    -POST请求 request.POST有值 request.GET也可能有值 
    -url中携带的参数在request.GET中

5.模板引擎中的特殊标记
    login.html中
        {{name}}
        {{users.0}} 列表的索引
        {{users.1}}
        {{user_dict.k1}} 取值字典
        {{user_dict.k2}}
        {% for row in user_list_dict %} 利用循环取字典 ,可以与html标签一起使用
            <p>row.id</p>
            <p>row.name</p>
            <p>row.email</p>
        {% endfor %}

    def login(request):
        return render(request,'xxx.html',{'name':'alex'}) 将name渲染成alex
        return redirect('/index/') 跳转到自己网站中的某个网页，可以不写前缀
        若templates下面还有目录，则在render中 要加目录名字/xxx.html

        return render(
            request,
            'index/index.html',
            {
                'name':'alxe',
                'users':['apple','lijie']
                'user_dict':{'k1':'v1','k2':'v2'}
                'user_list_dict':[
                    {'id':1,'name':'alex','email':'aaa@a.com'},
                    {'id':2,'name':'tom','email':'bbb@a.com'},
                ]
            }

        )


6.基于django + pymsql 实现登录

    
