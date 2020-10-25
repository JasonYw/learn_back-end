from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form
from django.forms import fields
import json



class LoginForm(Form):
    username =fields.CharField(
        required=True,
        min_length=3,
        max_length=15,
        error_messages ={
            "required":"用户名不能为空",
            "min_length":"用户名小于最小长度",
            "max_length":"用户名大于最大长度"
        }
    )
    password =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码不能为空",
            "min_length":"密码小于最小长度",
            "max_length":"密码大于最大长度"
        }
    )

class RegisterForm(LoginForm):
    password_again =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码前后不一致",
            "min_length":"密码前后不一致",
            "max_length":"密码前后不一致",
        }
    )
   
class RegisterForm_1(Form):
    username =fields.CharField(
        required=True,
        min_length=3,
        max_length=15,
        error_messages ={
            "required":"用户名不能为空",
            "min_length":"用户名小于最小长度",
            "max_length":"用户名大于最大长度"
        }
    )
    password =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码不能为空",
            "min_length":"密码小于最小长度",
            "max_length":"密码大于最大长度"
        }
    )

    password_again =fields.CharField(
        required=True,
        min_length=3,
        max_length=30,
        error_messages ={
            "required":"密码前后不一致",
            "min_length":"密码前后不一致",
            "max_length":"密码前后不一致",
        }
    )
    email =fields.EmailField(
        error_messages={
            "invalid":"email格式不正确"
        }
    )
    phone =fields.RegexField(
        '138\d+',
        error_messages={
            "invalid":"手机号格式不正确"
        }
    )


def login(request):
    if request.method =="GET":
        return render(request,"login.html")
    if request.method =="POST":
        logininfo =LoginForm(request.POST)
        '''
        #is_valid
        内部工作：
            1.每一次对FORM子类的实例化时，
                先把子类的字段放到self.fields={
                    'username':正则表达式，
                    'password'：正则表达式
                }
            2.循环self.fields:
                flag =True
                errors
                clened_data
                for key,v in self.fields.items():
                    key是字符串
                    v是正则表达式
                    input_value =request.POST.get(key)
                    正则表达式和input_value
                    if 正则与input_value不匹配:
                        flag =False
                return flag
        '''
        if logininfo.is_valid():
            if logininfo.cleaned_data.get("username") =="root" and logininfo.cleaned_data.get("password")=="0125":
                return HttpResponse("200")
            return render(request,"login.html",{"wrong":"用户名密码错误"})
        else:
            return render(request,"login.html",{"obj":logininfo})

def ajaxlogin(request):
    ret ={
        'status':True,
        'message':None,
    }
    logininfo =LoginForm(request.POST)
    if logininfo.is_valid():
        print(logininfo.cleaned_data.get("username"))
        print(request.POST)
    else:
        ret['status'] =False
        ret['message'] =logininfo.errors
        #print(logininfo.errors) #logininfo.errors 可以转换成json
        #jsdata =json.dumps(logininfo.errors)
        #print(jsdata)
    return HttpResponse(json.dumps(ret))


def register(request):
    registerinfo =RegisterForm(request.POST)
    if registerinfo.is_valid():
        if registerinfo.cleaned_data.get("password") == registerinfo.cleaned_data.get("password_again"):
            return HttpResponse("200")
    return redirect("/login/")

def register_1(request):
    if request.method =='GET':
        obj =RegisterForm_1()
        return render(request,'register_1.html',{"obj":obj})
    if request.method =='POST':
        obj =RegisterForm_1(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
        return render(request,'register_1.html',{"obj":obj})



class TestForm(Form):
    t1 =fields.CharField(
        required=True,
        max_length=8,
        min_length=2,
        #=====================================以下生成html用
        # widget=None, #自动生成HTML标签  选择生成input select textarea
        # label='label', #前端 {{obj.t1.label}} 就可以拿到这个值
        # label_suffix='----》',
        # initial='666', #
        # help_text='help_text',
        # #localize= ,#是否支持本地化，比如时间转化
        # disabled=True, #是否可以编辑
        #====================================以上注释要放在一起用,可以拼接成html标签
        #validators=[],#自定义验证规则
        error_messages={
            "required":"不能为空",
            "min_length":"小于最小长度",
            "max_length":"大于最大长度",
        }
    )
    
    t2 =fields.IntegerField(
        #默认required =True
        #若格式错误则是key为invalid
        #max_value min_value 指的不是长度，是数字大小
        max_value=1000,
        min_value=10,
        error_messages={
            "required":"t2不能为空",
            "invalid":"t2格式错误",
            "min_value":"t2必须大于10",
            "max_value":"t2必须小于1000"
        }
    )
    # t3 =fields.EmailField(
    #     #EmailField继承了CharField，所以CharField有的规则他都有

    #     error_messages={
    #         "required":"t3不能为空",
    #         "invalid":"t3必须是email格式"
    #     }
    # )
    # t4 =fields.URLField()
    # t5 =fields.SlugField()
    # t6 =fields.GenericIPAddressField()
    # t7 =fields.DateTimeField()
    # t8 =fields.DateField()
    # t9 =fields.RegexField(
    #     #第一个参数为正则表达式，自定制正则表达式
    #     #继承了charfield
    #     #是否为空
    #     #最大最短长度
    #     #错误信息
    #     r'139\d+', 
    #     error_messages={
    #         'invalid':"t9格式错误",
    #     }
    # 
    # ) 



def test(request):
    if request.method =="GET":
        obj =TestForm()
        return render(request,'test.html',{'obj':obj})
    if request.method =="POST":
        obj =TestForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
    return render(request,'test.html',{"obj":obj})
        
