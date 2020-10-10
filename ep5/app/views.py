from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views import View

# Create your views here.
def test(request):
    '''
        get 查
        post 创建
        delete 删除
        put 更新 
        html里 form表单 只有get和post
        ajax里 有其他的方式
    '''
    return HttpResponse('....')

class login(View): 
    '''
        from django.views import View
        需要继承
        优先执行 dispach 本质是getattr
        getattr() 函数用于返回一个对象属性值。
        所以可以做成装饰器
    '''

    def dispatch(self,request,*args,**kwargs):
        print('before')
        obj =super(login,self).dispatch(request,*args,**kwargs)
        print('after')
        return obj 

    def get(self,request):
        return render(request,'login.html')
 
    def post(self,request):
        print(request.POST.get('user'))  
        return HttpResponse('Login.post')
    
     