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


            