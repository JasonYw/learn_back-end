import socket

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
    
    if url == "/x":
        #加response响应体
        conn.send(b'123123')
    else:
        #加response响应体
        conn.send(b'404')

    #关闭连接
    conn.close()



