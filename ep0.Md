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
        对于ORM框架，是把类，对象，转换为sql语句，再通过pysql执行
        
        
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

2.自己开发web框架
    -socket
    -http协议
    -HTML知识
    -数据库(pymysql,SQLAlchemy)

3.Django框架

