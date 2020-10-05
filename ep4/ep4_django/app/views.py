from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.urls import reverse

# Create your views here.


def index(rquest):
    '''
        reverse 用来生成url
        urls 中 path('index/',views.index,name="n1")
        v等于/index/
    
        urls中 re_path(r'index/(\d+)',views.index,name="n1"),
        reverse('n1',args=(1,)) 生成/index/1

        urls中 re_path(r'index/(?P<a1>\d+)',views.index,name="n1"),
        reverse('n1',kwargs={'a1':111}) 生成/index/111

    '''
    user_list=[
        'alex','eric','tony'
    ]
    
    # v =reverse('n1',args=(1,)) 
    # v =reverse('n1',kwargs={'a1':111}) 
    # print(v)
    return render(rquest,'index.html',{'user_list':user_list})

# def edit(request):
#     return HttpResponse('....')
'''
re_path(r'edit/(\w+)/(\w+)/',views.edit) 第一在路由中的参数需要按照顺序
re_path(r'edit/(?P<a1>\w+)/(?P<a2>\w+)/',views.edit) 第二种不需要按照顺序，因为已经指定了 
以上两种 要统一用法！！！！，要不然会报错


re_path(r'edit/(\w+)/(?P<a2>\w+)/',views.edit) 搭配以下这种
def edit(request,a1,a2):这种会报错，会提示缺少一个参数a1
    print(a1,a2)
    return HttpResponse(a1+a2)

def edit(request,*args,**kwargs): 这种会报错，会提示缺少一个参数a2
    print(a1,a2)
    print(args,**kwargs)
    return HttpResponse(a1+a2)


re_path(r'edit/',views.edit) 表示 以edit/开头的url  搭配以下这种
def edit(request,*args,**kwargs): 不会报错 因为上面是正则表达式
    print(a1,a2)
    print(args,**kwargs)
    return HttpResponse(a1+a2)


re_path(r'edit$',views.edit) 表示 以edit开头的url 但是$为终止符，所以url只能是edit 推荐使用终止符


re_path(r'edit/(\w+).html$',views.edit) 只是一个正则表达式的模板，必须也要匹配上html 尤其是在html中
伪静态：
    -.html结尾的一般为静态网站
    -静态网站速度块，seo也会更高
    -动态网站拿到模板 再去数据库 在渲染 慢

'''
def edit(request,a1=None,a2=None):
    print(a1,a2)
    return HttpResponse(a1)


def login(request):
    return render(request,'login.html')

