from django.shortcuts import render,HttpResponse,redirect
import json
# Create your views here.

'''
class  jsonresposne():
    def __init__(self,req,status,msg):
        self.req =req
        self.status =status
        self.msg =message

    def render(self):
        #self.req
        #...
        #...
        
            可以写业务代码
            依赖中间件的process_template_response

        ret ={
            'status':self.status,
            'msg':self.msg,
        }

        return HttpResponse(json.dumps(ret))


def test(request):
    print('test')
    #int('asdadsad')
    
    return jsonresposne(request,True,'错误信息')
'''


def test(request):
    print('test')
    #int('asdadsad')
    
    return HttpResponse('200ok')


'''
form组件
'''

from django.forms import Form
from django.forms import fields
class LoginForm(Form):
    #长度，否为空的校验
    #正则验证
    username =fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            'required':"用户名不能为空",
            'min_length':"太短了",
            "max_length":"太长了",
        }
    )
    #正则验证
    password =fields.CharField(
        max_length=16,
        min_length=5,
        required=True,
        error_messages={
            'required':"用户名不能为空",
            'min_length':"太短了",
            "max_length":"太长了",
        }
    )
    #email =fields.EmailField() 验证邮箱
    #ip =fields.GenericIPAddressField() 验证ip
    #interger =fields.IntegerField() 验证数字
    


def login(request):
    '''
        用户名不能为空，长度为6-18，必须邮箱格式
        密码不能为空，长度5-16，必须包含下滑线数字
    '''
    if request.method == "GET":
        return render(request,'login.html')
    if request.method =="POST":
        obj =LoginForm(request.POST)
        if obj.is_valid(): #is_valid() 表示是否校验成功 -->返回True或者Flase 表示用户表单提交格式正确
            print(obj.cleaned_data) #obj.cleaned_data 字典类型 存储的request.POST
            #若需要入库的时候，则models.TABLE.objects.create(**obj.cleaned_data)
            #错误信息也被django做好了,存在obj.errors
            return HttpResponse("200ok")
        else:
            '''
            obj.errors获取所有的错误信息
            obj.errors['username'] 获取用户名的错误信息
            obj.errors['password'] 获取密码的错误信息
            obj.errors['username'][0] 获取username第一个错误信息，有错误信息永远取第一个
            obj.errors['password'][0] 获取password第一个错误信息，有错误信息永远取第一个
            注意：若没有错误信息，这样写会报错
            传到前端只传obj
            '''
            #print(obj.errors['username'][0])
            #print(obj.errors['password'][0])
            #
            return render(request,'login.html',{"obj":obj})



      
    #     if username =="root" and password=="0125":
    #         return HttpResponse('200ok')
    # return render(request,'login.html',{"error":"用户名或密码错误"})

