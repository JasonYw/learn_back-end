内容回顾：
    1.web框架的本质
        -本质socket
        -http协议
            -头
            -体
        -模板引擎的渲染在服务器端进行
        -本质传输的是字符串
    2.Django
        -安装
        -django-admin startproject mysite
        -配置
            -模板的路径
            -静态文件的路径
            -注释csrf，在中间件里
        -urls.py
            -url -> 函数
        -函数
            要求至少有一个参数为request，包含请求所有的数据
            -def index(request)
            -request.method
            -request.GET
            -request.POST
            -return HttpResponse(...)
            -return render(request,'模板路径',{})
            -return redirect('URL')
        -模板的渲染
            def index(request):
                return render(
                    request,
                    '模板的路径',
                    {
                        'k1':'v1',
                        'k2':[1,2,3,4],
                        'k3':{'k1':'v1'},
                    }
                )

            index.html
                <h1>{{k1}}<h1>
                <p>{{k1.1}}</h1>
                {% for i in k2 %}
                    <p>{{i}}</p>
                {% endfor %}
                <p>{{k3.k1}}</p>

内容回顾
    1.创建django程序
    2.新url方式：
        -添加
        -编辑
        -删除
    
    3.做一对多的关系
        班级表 学生表
        学生管理
        上述功能 需要对客户端行为进行判断
    
    4.模态对话框
        -班级管理
            -添加
                FROM 表单提交，页面会刷新
    AJAX
        -引入jquery
        -$.ajax({
            url:'要提交的地址'，
            type:'POST',//GET或者POST，提交的方式
            data:{'k1':'v1','k2':'v2'},//提交的数据
            success:function(data){
                //当前服务端处理完毕之后，自动执行的回调函数
                //data为返回的数据
                //使用ajax提交，后端return redirct、render 都无法完成页面跳转操作，需要使用Location.href操作
                Location.href="要跳转的地址"
            }
        })

        其他：
            1.模板语言if条件语句
            2.FORM表单提交，页面会刷新
            3.AJAX提交页面不刷新
            4.js实现页面跳转：
                location.href ="要跳转的地址"
            5.
                模态对话框一般都用 ajax进行绑定
                    -少量输入框，下拉框
                    -数据少
                    登录
                新url方式
                    -数据大操作多 
                    -对于大量的数据以及操作是适用的
                    
        作业：
            1.班级：
                Ajax删除
                Ajax编辑
            一对多的对话框实现


内容回顾
    1.web框架的本质
        浏览器（socket客户端）
            2.发送IP和端口 http://www.baidu.com:80/index/
                GET：
                    请求头
                        http1.1 /index/
                        。。。

                    请求体(无内容)
                
                POST：
                    请求头
                        http1.1 /index?p=123
                        ...
                    请求体
                        ...

        服务端（socket服务端）
            1.服务端启动并监听ip和端口，等待用户连接
            3.接收处理，并返回
                普通返回：
                    响应头：
                        access-control-allow-origin: *
                        cache-control: max-age=14400
                        content-type: application/javascript; charset=utf-8
                        date: Mon, 28 Sep 2020 15:10:33 GMT
                        etag: W/"5f2c2f77-54fd"
                        expires: Mon, 28 Sep 2020 03:12:26 GMT
                        last-modified: Thu, 06 Aug 2020 16:27:35 GMT
                        server: cloudflare
                        status: 200
                        vary: Accept-Encoding
                    响应体
                        html文件
            4.接受响应
                普通响应：页面直接显示 一次http请求
                重定向响应：再发起一次http请求

            
            重定向返回：（只有响应头，但是会多一个location）全是浏览器做的，服务端只做了返回
                响应头：
                    loacation：
                    access-control-allow-origin: *
                    cache-control: max-age=14400
                    content-type: application/javascript; charset=utf-8
                    date: Mon, 28 Sep 2020 15:10:33 GMT
                    etag: W/"5f2c2f77-54fd"
                    expires: Mon, 28 Sep 2020 03:12:26 GMT
                    last-modified: Thu, 06 Aug 2020 16:27:35 GMT
                    server: cloudflare
                    status: 200
                    vary: Accept-Encoding
            
                

    2.django的web框架
        a.创建project
            django-admin startproject mysite

        b.配置
            模板
            静态文件 加逗号
            csrf注释掉
        
        c.路由关系
            url -> 函数
        
        d.视图函数

            def index(request):
                request.method
                request.GET
                request.POST
                return HttpResponse(字符串内容)
                return render(request,'x.html(模板路径)',{}(模板渲染)) -> 本质 HttpResponse
                    #1.获取模板+数据，渲染
                    #2.HttpResponse()
                return redirect('url')

        e.模板渲染
            {{k1}}

            字典、list都是.
            {{k1.0}}
            {{k1.1}}

            {% for i in list %}
                {{i}}
            {% endfor %}

            {%if 1>2 %}

            {% endif %}

        
    3.Ajax
        不是django特有的，是一个单独的前端技术
        AJAX(jquery)

            $.ajax({
                url:'',
                type:'GET',
                data:'{k1:'v1'}',
                success:function(data){
                    //data 为请求ajax请求成功后，服务器的返回值，对于django来说 只能用return HttpResponse() 返回字符串
                    //data本质为字符串
                }
            })

    4.html 
        -若html中a标签内如果既有href 又有onclik 则优先执行onclick，执行后继续跳转到href
        -若不想让a标签中的href执行，只想执行完onclick之后停止则
            <a href="www.baidu.com" onclick="return example();"></a>
            <script>
                function example(){
                    //return false,则a标签执行完onclick中的example后，不会跳转到href
                    //相反若想让其跳转，return true即可
=
                    return false
                }
            </script>

    单表
        添加
        编辑
        删除

        a.阻止默认事件的发生
        b.location.reload()
        c.HttpResponse(json.dumps())
        d.json.parse()
    
    一对多
        students
        jquery绑定的事件 也可以阻止事件发生，在方法中return false即可
        $(function(){
            //当页面加载完成之后自动执行
            //也可以阻止事件发生
            $('#add_modal').click(function(){
                return false
            })
        })
    
    多对多

内容回顾：
    1.Http请求的生命周期
        请求头 -> 提取url ->路由关系匹配 -> 函数（模板加数据渲染）->返回用户（响应头+响应体）
    2.def index(request):
        request.method
        request.POST
        request.GET
        return Httpresponse
        return render
        return redirect
    3.
        {% for i in list%}
        {% endfor %}
        {% if %}
        {% endif %}
        索引.
        {{}}
    
    4.
        <html>
            <head>
            </head>
            <body>
                <script>
                    alert({{k1}})
                </script>
            </body>
        </html>
        render渲染工作本质就是替换，所以{{k1}}不管在哪都会替换 
        后端传递给{{k1}}为字符串，则alert({{k1}}) 会把其当成变量，会报错，
        所以避免报错，要alert('{{k1}}')
        alert() 出现的值为 后端给k1传递的值，而不是{{k1}}
        游览器拿到的页面是已经渲染后的结果
    
    5.js序列化
        阻止默认事件发生
            <a onclick="return func()">
            <script>
                func(){
                    return false
                }
            </script>
            jquery,绑定的事件直接在func中return false即可
    
    6.ajax
        $.ajax({
            url:'',
            type:'',
            data:{

            },
            dataType:'JSON',
            success:func(data){
                data=JSON.parse()  /转换成json
            }
        })

    7.封装SqlHelper

    8.AJAX发送数据
        若data对应的是列表，添加traditional：true
        data不支持字典，若发送字典，通过JSON.stringify() 更改
        $.ajax({
            url:'',
            type:'',
            data:{

            },
            tradational.true，
            dataType:'JSON',
            success:func(data){
                data=JSON.parse()  /转换成json
            }
        })


内容整理：
    -Bootstrap响应式布局：@meida()

    -栅格：
        12格
    
    -表格：
    
    -导航条：

    -路径导航

    -fontawesome

    -布局postion:absolute

    -xx:hover .xxxxx{  当鼠标移动xx样式上时，子标签xxxxx应用以下的属性
    }

    -django母版
        母版：
        <html>
            '''
                {% block xx %}
                {% endblock %}
            '''

        </html>
        子版：

                {% extends 'layout.html' %}
                {% block xx %}
                    '''
                {% endblock %}
    
    用户登录
        cookie 保存在游览器端的键值对，设置超时时间

                -发送http请求时，在请求头中携带可访问的cookie
                -响应头

        -django回写cookie
            def xx(request):
                obj =HttpResponse('...')
                obj.set_cookie(...)
                request.COOKIES.get(...)

                obj.set_signed_cookie(...,salt='')
                request.get_signed_cookie(....,salt='')  
                salt 为签名

        -自定义cookie签名
            正解反解都要自己写

        -装饰器装饰views中其他函数中


内容回顾：
    1.母版
        layout.html
            '''
            {% block x %}
            {% endblock %}
            '''

    2.子板
        index.html
            {% extends 'xxx.html' %}
            {% block x %}
                ...
            {% endblock %}
    
    3.cookie
        在浏览器上保存的键值对
        
        def index(request):
            request.COOKIES
            request.get_signed_cookie('k1',salt='')
            obj =render/HttpResponse/redirect
            obj.set_cookie(k1,v1,max_age)
            obj.set_signed_cookie(k1,v1,max_age,salt='')

    4.Bootstrap响应式布局
        -css
        -js 欠

    5.后台布局
        position：absolute 绝对
                fixed  相对于窗口
        hovar   .xx:hover .xxxx{

                }
        







今日作业：
    1.布局+代码
    2.登录cookie+装饰器
    3.布局页面的HTML加css

坦白：
    project
        -app01 自己创建的目录
            -views.py 通过命令可以创建
        -SQLHelper 封装SQL操作

    非主流的
        -1.创建app
        -2.数据库操作

    Django：
        -路由系统
        -视图函数
        -模板
        -ORM（类和表：对象-行；pymysql连接数据库） 操作数据库做了一个类和对象的映射

    Torando
        -路由
        -视图
        -模板
        -自由：pymysql sqlachemy
    
    flask
        pymysql sqlachemy


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
        
        a./login/ - def login
        b./add-user/(\d+) -> def add_user(request) 可加正则表达式
        




    1.路由系统
    2.视图函数 CBV，FBV
        FBV 视图基于函数
        CBV 视图基于类
    3.django的ORM操作




作业：
    学员管理
        把原生sql全部替换掉



学员管理：
    表：
        班级表(day 1)
            id title 
        学生
            id name class_id(FK)
        老师表(day 1)
            id name

        老师的表需要和班级建立关系
        一个老师可以教多个班级
        一个班级可以有多个老师
        多 对 多

        创建关系表
            id teacher_id class_id 

        3个角色4张表

今日内容：
    1.对话框
        单表
        一对多
    2.多对多
        -新url方式
            -增加
            -编辑
        -对话框
            -增加
            -编辑
                数组.indexof
            -遗留左右移动的方式

    3.Bootstrap 样式
        -bootstrap 第一讲
            -看图拷贝
            -常用的标签
            -响应式
            -js
        -fontawesome
            -比对图标做操作  

    4.fontawesome 图标  


    1.Bootstrap
        -一个包含CSS和JS的一个代码库
        -样式
        -响应式
            --根据窗口大小进行变化 css @media关键字
            --导航条
            --栅格
    
    2.完善学员管理系统
        -后台管理布局
        -Django母版
            母版：存放所有页面公用的
            子板：
                -继承母版
                -自定义当前页面私有的东西
    
    3.cookie
        -浏览器端保存的键值对，不是服务器端！！！
        -服务端可以修改客户端cookie，
        -游览器访问服务端是携带cookie的
        -cookie放在请求头中
        -cookie一般做用户登录

    应用
        -投票
        -用户登录
    
    set_cookie
        KEY,
        VALUE="",
        max_age cookie有效周期
        expires, cookie到期日
        path url限制
        domain 域名限制
        secure https
        httponly 无法在js中找到cookie，只能在http请求中传输，通过js代码无法获取到，通过抓包可以获得

    set_signed_cookie('key','vlue',salt='')
        -cookie的签名

    自定制签名
    装饰器
        
        






    单表操作：
        -增
        -删
        -改
        -查
    一对多操作：
        -增
        -删
        -改
        -查
    多对多操作：
        -增
        -删
        -改
        -查

