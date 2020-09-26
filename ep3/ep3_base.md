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