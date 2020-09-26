from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.shortcuts import render
from utils import sqlhelper
import time

def add_class(request):
    class_name =request.POST.get('title')
    if len(class_name) >0:
        class_num =sqlhelper.get_list('SELECT id FROM class ORDER BY id DESC LIMIT 1')
        if class_num ==[]:
            class_id =1
        else:
            class_id =class_num[0][0]+1
        sqlhelper.modify('INSERT IGNORE INTO class (id,title) VALUES (%s,%s)',[class_id,class_name,])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级不能为空')

    '''
    页面不刷新,提示错误信息
    若用form表单提交，这个功能无法完成
    form表单提交，页面必刷新
    若想完成此功能并且是对话框的方式就不能用form表单提交
    若用ajex提交，提交后无法用renturn 进行跳转，只能通过写js进行跳转
    在js中使用location.href完成跳转
    '''
