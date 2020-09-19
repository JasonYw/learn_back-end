import socket
import time
import mysql.connector

def f1(request):
    '''
        也需要获取用户提交的数据，所以可以把请求头请求体传进来
        处理用户请求并返回相应的内容
        request：用户请求所有的信息
    '''
    f =open('D:/py/py_django/ep1/dynamic_ep0/index.html','r',encoding='utf-8',errors='ignore')
    response =f.read()
    f.close()
    return(response)  #本质返回的是字符串

def f2(request):
    '''
        动态网页模板
        html为模板
        将html部分内容做替换，形成动态数据
    '''
    f =open('D:/py/py_django/ep1/dynamic_ep0/artical.html','r',encoding='utf-8',errors='ignore')
    response =f.read()
    f.close()
    ctime =time.time()
    response =response.replace('@@sw@@',str(ctime))
    return(response)

def f3(request):
    '''
        从数据库里取数据
        将数据写成html格式
        并作替换（模板的渲染）
    '''
    connector =mysql.connector.connect(user='root',password='0125',database='py_write')
    cursor =connector.cursor()
    cursor.execute('SELECT name,score,date FROM db_movie ORDER BY score DESC,date DESC;')
    movie_list =cursor.fetchall()
    cursor.close()
    connector.close()
    f =open('D:/py/py_django/ep1/dynamic_ep0/movie.html','r',encoding='utf-8',errors='ignore')
    response =f.read()
    f.close()
    movie_html_list=[]
    #movie_html =''
    for movie in movie_list:
        name ='<th>'+movie[0]+'</th>'
        score ='<th>'+str(movie[1])+'</th>'
        date ='<th>'+movie[2]+'</th>'
        # movie_html =movie_html +'<tr>'+name+score+date+'</tr>'
        movie_html ='<tr>'+name+score+date+'</tr>'
        movie_html_list.append(movie_html)
    # print(movie_html)
    content =''.join(movie_html_list)
    '''
        模板的渲染（模板加数据）
    '''
    response =response.replace('@@content@@',content)
    return(response)
    
def run(routers):
    sock =socket.socket()

    #绑定127.0.0.1并且绑定端口号
    sock.bind(('127.0.0.1',8888))

    #并且等5位客户端
    sock.listen(5)

    while True:

        #无人链接时会hold住，阻塞，除非有客户端来连接
        conn,addr =sock.accept()

        #当有人来连接时，获取用户发送的数据，8096为缓冲区大小,data为字节类型
        data =conn.recv(8096)

        #转成字符串
        data =str(data,encoding='utf-8') #转成字节 bytes(data,encoding='utf-8')

        #查看请求内容request，request的请求头与请求体
        print(data)

        #获取请求头，分割，通过判断请求来针对不同的请求返回不同的内容
        headers,bodys =data.split('\r\n\r\n')  #d第一步通过\r\n\r\n分割请求头和请求体
        temp_list =headers.split('\r\n') #分割请求头 
        method,url,protocal =temp_list[0].split(' ')#请求头第一行无':' 是请求的方法与url与http协议版本，靠空格分割
        # 从第二行开始靠':'分割

        #返回数据response
        #加response响应头
        conn.send(b'HTTP/1.1 200 OK \r\n\r\n')#若不加状态码可能导致部分游览器无法访问

        func_name =None
        for item in routers:
            if item[0] == url:
                func_name =item[1]
                break
        
        if func_name:
            response =func_name(data)
        else:
            response =b'404'

        try:
            response =bytes(response,encoding='utf-8') #从服务器端发送的也是二进制数据，所以要转换成二进制
        except:
            pass
    
        conn.send(response)
        #关闭连接
        conn.close()

def main():
    routers =[
        ('/x',f1),
        ('/xx',f2),
        ('/xxx',f3),
    ]
    run(routers)

if __name__ =="__main__":
    main()

