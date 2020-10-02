from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.shortcuts import render
from utils import sqlhelper
import time
import json

def add_class(request):
    '''
    页面不刷新,提示错误信息
    若用form表单提交，这个功能无法完成
    form表单提交，页面必刷新
    若想完成此功能并且是对话框的方式就不能用form表单提交
    若用ajex提交，提交后无法用renturn 进行跳转，只能通过写js进行跳转
    在js中使用location.href完成跳转
    '''
    class_name =request.POST.get('title')
    if len(class_name) >0:
        class_num =sqlhelper.get_list('SELECT id FROM class ORDER BY id DESC LIMIT 1;')
        if class_num ==[]:
            class_id =1
        else:
            class_id =class_num[0][0]+1
        sqlhelper.modify('INSERT IGNORE INTO class (id,title) VALUES (%s,%s);',[class_id,class_name,])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级不能为空')

def del_class(request):
    class_id =request.POST.get("class_id")
    if sqlhelper.modify('DELETE FROM class WHERE id =%s;',[class_id,]):
        return HttpResponse('200')
    else:
        return HttpResponse('404')
    
def edit_class(request):
    if request.method == "GET":
        class_id =request.GET.get("nid")
        class_name =sqlhelper.get_list('SELECT title FROM class WHERE id =%s LIMIT 1;',[class_id,])[0][0]
        return HttpResponse(class_name)
    if request.method == "POST":
        print(request.POST)
        class_id =request.POST.get('class_id')
        new_classname =request.POST.get("new_c_name")
        if new_classname == '':
            return HttpResponse('ERROR')
        sqlhelper.modify('UPDATE class SET title=%s WHERE id=%s;',[new_classname,class_id,])
        return HttpResponse('200')

def add_student(request):
    ret ={
        'status':True,
        'message':None,
    }
    name =request.POST.get("name")
    class_name =request.POST.get("class")
    if name =='':
        ret['status'] =False
        ret['message'] ='None type'
        return HttpResponse(json.dumps(ret))
    stu_num =sqlhelper.get_list('SELECT id FROM student ORDER BY id DESC LIMIT 1;')
    if stu_num ==[]:
        stu_num =1
    else:
        stu_num =stu_num[0][0] +1
    try:
        class_id =sqlhelper.get_list('SELECT id FROM class WHERE title=%s LIMIT 1;',[class_name])[0][0]
        sqlhelper.modify('INSERT INTO student (id,name,class_id) VALUES (%s,%s,%s);',[stu_num,name,class_id,])
    except Exception as e:
        ret['status'] =False
        ret['message'] =str(e)
    return HttpResponse(json.dumps(ret))

def edit_student(request):
    ret ={
        'status':True,
        'message':None,
    }
    if request.method == "POST":
        stu_id =request.POST.get("stu_id")
        new_name =request.POST.get("new_name")
        new_class =request.POST.get("new_class")
        if new_name =="":
            ret['status'] =False
            ret['message']='new name is empty'
            return HttpResponse(json.dumps(ret))
        class_id =sqlhelper.get_list('SELECT id FROM class WHERE title=%s LIMIT 1;',[new_class])[0][0]
        if sqlhelper.modify('UPDATE student SET name=%s ,class_id=%s WHERE id=%s;',[new_name,class_id,stu_id,]):
            return HttpResponse(json.dumps(ret))
        ret['status'] =False
        ret['message']='sql error'
        return HttpResponse(json.dumps(ret))

def del_student(request):
    ret ={
        'status':True,
        'message':None,
    }
    if request.method =="POST":
        stu_id =request.POST.get("stu_id")
        if sqlhelper.modify("DELETE FROM student WHERE id =%s",[stu_id,]):
            return HttpResponse(json.dumps(ret))
        else:
            ret['status'] =False
            ret['message'] ='sql error'
            return HttpResponse(json.dumps(ret))

def add_teacher(request):
    if request.method =="POST":
        ret={
            'status':True,
            'message':None
        }
        new_teacher =request.POST.get("title")
        class_list =request.POST.getlist("class_list")
        if ( new_teacher == "" or class_list ==None):
            ret['status'] =False
            ret['message'] ='empty data'
            return HttpResponse(json.dumps(ret))
        sql=sqlhelper.SqlHelper()
        teacher_id =sql.get_list("SELECT id FROM teacher ORDER BY id DESC LIMIT 1")
        if teacher_id ==[]:
            teacher_id =1
        else:
            teacher_id =teacher_id[0][0] +1 
        sql.modify('INSERT INTO teacher (id,name) VALUES (%s,%s)',[teacher_id,new_teacher])
        num =sql.get_list("SELECT id FROM link_t_C ORDER BY id DESC LIMIT 1")
        if num ==[]:
            num =1
        else:
            num =num[0][0] +1 
        for i in class_list:
            sql.modify('INSERT INTO link_t_C (id,teacher_id,class_id) VALUES (%s,%s,%s)',[num,teacher_id,int(i)])
            num =num+1
        return HttpResponse(json.dumps(ret))

def del_teacher(request):
    ret={
        'status':True,
        'message':None
    }
    teacher_id =request.GET.get("teacher_id")
    sql =sqlhelper.SqlHelper()
    sql.modify('DELETE FROM teacher WHERE id=%s',[teacher_id])
    sql.modify('DELETE FROM link_t_C WHERE teacher_id=%s',[teacher_id])
    sql.close()
    return HttpResponse(json.dumps(ret))

def edit_teacher(request):
    ret={
        'status':True,
        'message':None
    }
    teacher_id =request.POST.get("teacher_id")
    teacher_name =request.POST.get("teacher_name")
    classid_list =request.POST.getlist("class_list")
    if (teacher_name =="" or classid_list ==[]):
        ret={
            'status':False,
            'message':"empty message"
        }
        return HttpResponse(json.dumps(ret))
    sql =sqlhelper.SqlHelper()
    sql.modify("UPDATE teacher SET name=%s WHERE id=%s",[teacher_name,teacher_id])
    sql.modify("DELETE FROM link_t_C WHERE teacher_id=%s",[teacher_id,])
    num =sql.get_list("SELECT id FROM link_t_C ORDER BY id DESC LIMIT 1")
    if num ==[]:
        num =1
    else:
        num =num[0][0]+1
    for class_id in classid_list:
        sql.modify("INSERT INTO link_t_C (id,teacher_id,class_id) VALUES (%s,%s,%s)",[num,teacher_id,class_id])
        num =num+1
    sql.close()
    return HttpResponse(json.dumps(ret))

def add_1_teacehr(request):
    sql =sqlhelper.SqlHelper()
    class_list =sql.get_list("SELECT * FROM class")
    sql.close()
    return HttpResponse(json.dumps(class_list))