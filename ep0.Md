1.数据源
    1.安装
    2.创建用户
    3.授权
    4.访问
        -连接
            -数据库
                终端创建数据库（字符编码）
            -数据表
                利用终端创建数据表
                利用ORM数据表
                利用pymysql创建数据表
                    CREATE ...)engine=innodb innodb特性支持事务
            -数据行
                增
                删
                改
                查
                    -LIMIT（优化，分页）数据量大的时候分页的时候很慢
                    -GROUP BY
                    -ORDER BY
        -关闭

    问题：简述ORM原理
        对于使用ORM框架的用户，目的是不让用户写sql语句，通过类和对象的方式以及内部提供的方法来进行数据库操作
        对于ORM框架，是把类，对象，转换为sql语句，再通过pymysql连接，执行


        class User：
            def __init__(self):
                self.id
                self.name
                self.email
            
            def order_by():

        obj =User()
        obj.__dict__ ={
            id:'',
            name:'',
            email:
        }
        
        用上述类实现下面的sql语句

        SELECT id,name,email FROM user ORDER BY...;

        ps:
            code first(*)  db first

2.自己开发web框架
    -socket
    -http协议
        HTTP：
            无状态、短链接
        TCP:
            不断开
        WEB应用（网站）：
        
            浏览器（socket客户端）
                2.在浏览器上属于域名，经过DNS服务器变成ip地址（42.121.252.58.80），并指定端口号默认为80
                    sk.socket()
                    sk.connect((42.121.252.58.80))
                    sk.send(request)
                5.接收response
                6.连接断开sk.close()
                

            网站（socket服务端）
                1.监听自己的ip以及端口（42.121.252.58.80）
                    while TRUE：
                        等待用户连接
                        3.收到request
                        4.response
                        用户断开


        http建立在tcp之上，有来有回基于tcp，http请求是无状态的短链接

        发送：
            请求头+两个换行+请求体：
            GET / HTTP/1.1
            Host: 127.0.0.1:8888
            Connection: keep-alive
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            Sec-Fetch-Site: none
            Sec-Fetch-Mode: navigate
            Sec-Fetch-User: ?1
            Sec-Fetch-Dest: document
            Accept-Encoding: gzip, deflate, br
            Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
            

            内容（若请求为POST 则发送的参数就放在内容里）

        响应：（响应头） 用户在页面上看到的内容本质上是字符串，是响应体，又因为有css，js以及游览器解析出来的。
            200 OK
            Bdpagetype: 1
            Bdqid: 0xaff87efa000c9d36
            Cache-Control: private
            Connection: keep-alive
            Content-Encoding: gzip
            Content-Type: text/html;charset=utf-8
            Date: Sat, 19 Sep 2020 13:25:32 GMT
            Expires: Sat, 19 Sep 2020 13:25:26 GMT
            Server: BWS/1.1
            Set-Cookie: BDSVRTM=0; path=/
            Set-Cookie: BD_HOME=1; path=/
            Set-Cookie: H_PS_PSSID=7509_32617_1428_7544_32328_31254_7579_32706_7551_7606_32116_7564_26350_22157; path=/; domain=.baidu.com
            Strict-Transport-Security: max-age=172800
            Traceid: 1600521932020362625012680024363069381942
            Transfer-Encoding: chunked
            X-Ua-Compatible: IE=Edge,chrome=1




    -HTML知识
    -数据库(pymysql,SQLAlchemy)
   

3.Django框架

