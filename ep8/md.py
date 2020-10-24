from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class M1(MiddlewareMixin):
    def process_request(self,request):
        print("m1.request")
    
    def process_view(self,request,callback,callback_args,callback_kwargs):
        '''
        callback 等效于 视图函数view_func
        '''
        #print("m1",callable,callback_args,callback_kwargs)
        #return callback(*callback_args,**callback_kwargs)
        print('m1.process_view')
        #return callback(request,*callback_args,**callback_kwargs)

    def process_response(self,request,response):
        print("m1.response")
        return response

    def process_exception(self,request,exception):
        print("m1.process_exception")

    def process_template_response(self,request,response):
        '''
            对视图函数的返回值有要求，如果有render方法这个函数才被调用
        '''
        print("m1.process_template_response")
        return response
    

class M2(MiddlewareMixin):
    def process_request(self,request):
        print("m2.request")

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('m2.process_view')
        #return callback(request,*callback_args,**callback_kwargs)
        
    def process_response(self,request,response):
        print("m2.response")
        return response

    def process_exception(self,request,exception):
        print("m2.process_exception")
        return HttpResponse("错误了")
    