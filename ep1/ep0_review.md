1.HTTP，无状态，短链接，发送响应后直接断开
2.浏览器是socket客户端，网站是socket服务端
3.自己写网站
    a.socket服务端
    b.根据url不同返回不同的内容
        路由系统：
            url --> 函数
    c.给用户返回的response本质为字符串
        模板引擎渲染：
            HTML充当模板（特殊字符）
            自己创造任意数据
        返回字符串
4.web框架：
    框架种类：
        -a,b,c            --> Tornado
        -[第三方a],b,c    -->django属于第二类，wsgiref -> django  ps:django没有自己的socket服务端，用的是python的wsgiref模块做的socket服务端，django做的b和c
        -[第三方a],b,[第三方c] -->flask c用的是jinja2

    框架另一个维度的分类:
        -Django框架
        -其他


