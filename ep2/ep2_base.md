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

      

