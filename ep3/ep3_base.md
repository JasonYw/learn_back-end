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

        阻止默认事件的发生
            



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

    3.Bootstrap 样式

    4.fontawesome 图标

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



Django基础
前端知识

