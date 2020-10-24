from wsgiref.simple_server import make_server
def login():
    return 'login'

def RunServer(environ,start_response):
    start_response('200 ok',('Content-Type','text/html'))
    url =environ['PATH_INFO']
    urlpatterns =(
        ('/index/',index),
        ('/login/',login)
    )
    func =None
    for item in urlpatterns:
        if item[0] ==url:
            func =item[1]
            break

    if func:
        return func()
    else:
        return [b'404 not found']
    
if __name__ == '__main__':
    httpd =make_server("",800,RunServer)
    httpd.server_forever()