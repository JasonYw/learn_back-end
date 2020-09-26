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

    #查看请求内容request，request的请求头与请求体
    print(data)

    conn.send(b'HTTP/1.1 200 OK \r\n\r\n')
    
    #返回数据response
    #加response响应头
    conn.send(b'HTTP/1.1 200 OK \r\n\r\n') #若不加状态码可能导致部分游览器无法访问

    #加response响应体
    conn.send(b'123123')
    
    #关闭链接
    conn.close()





