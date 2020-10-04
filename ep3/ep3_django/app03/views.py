from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from utils import sqlhelper
import json
import datetime
from datetime import timedelta

def test(request):
    return render(request,'test.html')

def layout(request):
    return render(request,'layout.html')

def index_(request):
    # if request.GET.get("href") =='class':
    #     return redirect('/class/')
    # elif request.GET.get("href") == 'teacher':
    #     return redirect('/teacher/')
    # elif request.GET.get("href") == 'student':
    #     return redirect('/student/')
    # else:
    return redirect('/login/')

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        try:
            user =request.POST.get("email")
            passwd =request.POST.get("password")
            print(user,passwd)
            if (user =='' or passwd ==''):
                raise Exception('empty data')
            sql =sqlhelper.SqlHelper()
            user_data =sql.get_list('SELECT email,passwd FROM user_passwd WHERE email=%s LIMIT 1',[user,])
            if user_data ==[]:
                raise Exception('user not create')
            if (user == user_data[0][0] and  passwd ==user_data[0][1]):
                obj =redirect('/class/')
                obj.set_signed_cookie('ticket','cookie',max_age=10,salt='jjjjj') #max_age 超时时间单位s 推荐max_age
                return obj
                '''
                key: str,
                value: str = ...,
                max_age: Optional[int] = ..., 超时时间 s为单位
                expires: Optional[Union[str, datetime.datetime]] = ..., 具体的超时日期
                path: str = ..., path='/url' 表示只能在某一个url中有效 若url只有一个/ 则所有的url都可以读取到
                domain: Optional[str] = ..., 表示只访问某个域名才可以读到的cookie 统一认证登录会用到
                secure: bool = ..., https相当与有证书，跟https相关，若走https协议在把secure改为true
                httponly: bool = ..., 当httponly=ture时表示用js代码无法获取cookie 用户没有权限对cookie进行操作，只给http来回发请求才可以用，无法在js找到

                obj.set_signed_cookie()  //对cookie加密 给salt加参数
                request.get_signed_cookie('ticket'，'jjjjj') //获取加密cookie 要把salt传入
                
                
                
                ct =datetime.datetime.utcnow()  #当前时间
                v =timedelta(seconds=10)
                value =ct+v #表示当前时间加10S
                obj.set_cookie('ticket','cookie',expires=value)
                
                
                
                obj =HttpResponse('ok') 响应体
                obj.set_cookie('k1','v1') 响应头
                return obj

                obj =render(request,'xxx.html')
                obj.set_cookie('k1','v1') 
                return obj


                '''

                
            raise Exception('wrong user or password')
        except Exception as e:
            return redirect('/login/')


def classes(request):
    '''
    去请求的cookie中获取凭证
    tk =request.COOKIES.get("ticket")
    if not tk:
        return redirect('/login/')
    '''
    tk =request.get_signed_cookie('ticket','jjjjj')
    if not tk:
        return redirect('/login/')

    class_list =sqlhelper.get_list("SELECT * FROM class;")
    return render(request,'class.html',{'class_list':class_list})

def add_class(request):
    
    if request.method =="GET":
        return render(request,'add_class.html')
    else:
        class_name =request.POST.get('title')
        class_num =sqlhelper.get_list('SELECT id FROM class ORDER BY id DESC LIMIT 1;')
        if class_num ==[]:
            class_id =1
        else:
            class_id =class_num[0][0]+1
        sqlhelper.modify('INSERT IGNORE INTO class (id,title) VALUES (%s,%s);',[class_id,class_name,])
        return redirect('/class/')

def del_class(request):
    class_id =request.GET.get("nid")
    if sqlhelper.modify("DELETE FROM class WHERE id =%s;",[class_id,]):
        return redirect('/class/')
    else:
        return redirect('/class/')

def edit_class(request):
    if request.method == "GET":
        class_id =request.GET.get("nid")
        class_title =sqlhelper.get_list('SELECT title FROM class WHERE id =%s LIMIT 1;',[class_id])
        return render(request,'edit_class.html',{'result':[class_id,class_title[0][0]]})
    if request.method == "POST":
        class_id =request.GET.get("nid")
        class_title =request.POST.get("class_title")
        if class_title =='':
            return redirect('/del_class/?nid='+class_id)
        sqlhelper.modify("UPDATE class SET title=%s WHERE id=%s;",[class_title,class_id])
        return redirect('/class/')
 
def teacher(request):
    teacher_list =sqlhelper.get_list('''
            SELECT  l.id,t.id teacher_id,t.name,c.id class_id,c.title FROM teacher t
            LEFT JOIN link_t_C l ON t.id =l.teacher_id
            LEFT JOIN class c ON l.class_id =c.id;''',[]
        )
    class_list =sqlhelper.get_list('SELECT * FROM class')
    dict_ ={}
    for key in teacher_list:
        if dict_.get(key[1]) ==None:
            dict_[key[1]] ={
                'name':key[2],
                'titles':[key[4],],
                'teacher_id':key[1]
            }
        else:
            dict_[key[1]]['titles'].append(key[4])
    return render(request,'teacher.html',{'teacher_list':dict_.values(),'class_list':class_list})

def add_teacher(request):
    if request.method =="GET":
        class_list =sqlhelper.get_list("SELECT * FROM class")
        return render(request,'add_teacher.html',{"class_list":class_list})
    if request.method =="POST":
        teacher_name =request.POST.get("teacher_name")
        class_list =request.POST.getlist("class_list")
        if teacher_name =="":
            class_list =sqlhelper.get_list("SELECT * FROM class")
            return render(request,'add_teacher.html',{"class_list":class_list,"error":"empty name"})
        teacher_id =sqlhelper.get_list('SELECT id FROM teacher ORDER BY id DESC LIMIT 1;')
        if teacher_id ==[]:
            teacher_id =1
        else:
            teacher_id =teacher_id[0][0] +1
        sqlhelper.modify("INSERT INTO teacher (id,name) VALUES (%s,%s);",[teacher_id,teacher_name])
        for class_id in class_list:
            num =sqlhelper.get_list("SELECT * FROM link_t_C ORDER BY id DESC LIMIT 1;")
            if num==[]:
                num =1
            else:
                num =num[0][0]+1
            sqlhelper.modify("INSERT INTO link_t_C (id,teacher_id,class_id) VALUES (%s,%s,%s)",[num,teacher_id,int(class_id),])
        return redirect('/teacher/')


def del_teacher(request):
    teacher_id =request.GET.get('nid')
    sqlhelper.modify('DELETE FROM link_t_C WHERE teacher_id=%s;',[teacher_id,])
    sqlhelper.modify('DELETE FROM teacher WHERE id=%s;',[teacher_id,])
    return redirect('/teacher/')

def edit_teacher(request):
    if request.method =='GET':
        sql =sqlhelper.SqlHelper()
        teacher_id =request.GET.get("nid")
        teacher =sql.get_list('SELECT * FROM teacher WHERE id =%s LIMIT 1;',[teacher_id])
        class_id =sql.get_list('SELECT * FROM link_t_C WHERE teacher_id =%s;',[teacher_id,])
        class_list =sql.get_list('SELECT * FROM class;')
        class_data=[]
        for cid in class_id:
            print(cid)
            class_data.append(sql.get_list('SELECT * FROM class WHERE id=%s LIMIT 1',[cid[2],]))
        sql.close()
        return render(request,'edit_teacher.html',{'teacher_id':teacher_id,'teacher_name':teacher[0][1],'class_data':class_data,'class_list':class_list,})
        # 1 [(1, 'tony2')] [[(1, 'class_1')], [(2, 'class_2')]]
    if request.method == 'POST':
        teacher_id =request.GET.get("nid")
        teacher_name =request.POST.get("teacher_name")
        class_selected =request.POST.getlist('class_list')
        if (teacher_name == "" or  class_selected==[]):
            return redirect('/teacher/')
        print(class_selected)
        sql =sqlhelper.SqlHelper()
        link_id =sql.get_list('SELECT id FROM link_t_C WHERE teacher_id=%s',[teacher_id,])
        print(link_id)
        sql.modify('UPDATE teacher SET name=%s WHERE id=%s',[teacher_name,teacher_id,])
        sql.modify('DELETE FROM link_t_C WHERE teacher_id=%s',[teacher_id,])
        num =sql.get_list("SELECT id FROM link_t_C ORDER BY id DESC LIMIT 1")
        if num ==[]:
            num =1
        else:
            num =num[0][0]+1
        for i in class_selected:
            sql.modify('INSERT link_t_C (id,teacher_id,class_id) VALUES (%s,%s,%s)',[num,teacher_id,int(i)])
            num =num+1
        sql.close()
        return redirect('/teacher/')

def student(request):
    student_list =sqlhelper.get_list('SELECT s.id,s.name,c.title class,c.id FROM student s LEFT OUTER JOIN class c ON s.class_id =c.id;')
    class_list =sqlhelper.get_list('SELECT * FROM class;')
    return render(request,"student.html",{'student_list':student_list,'class_list':class_list,})


def add_student(request):
    if request.method =="GET":
        class_list =sqlhelper.get_list('SELECT * FROM class;')
        return render(request,"add_student.html",{'class_list':class_list})
    if request.method =="POST":
        class_id =request.POST.get("class_id")
        if len(class_id) >0:
            student_name =request.POST.get("student_name")
            student_id =sqlhelper.get_list('SELECT id FROM student ORDER BY id DESC LIMIT 1;')
            if student_id == []:
                student_id = 1
            else:
                student_id = student_id[0][0]+1
            sqlhelper.modify('INSERT INTO student (id,name,class_id) VALUES (%s,%s,%s);',[student_id,student_name,class_id])
            return redirect('/student/')
        else:
            return render(request,"add_student.html")

def del_student(request):
    student_id = request.GET.get("nid")
    sqlhelper.modify("DELETE FROM student WHERE id=%s;",[student_id])
    return redirect('/student/')


def edit_student(request):
    if request.method == 'GET':
        class_list =sqlhelper.get_list('SELECT * FROM class;')
        student_id =request.GET.get("nid")
        student =sqlhelper.get_list('SELECT * FROM student WHERE id=%s LIMIT 1;',[student_id,])[0]
        class_name =sqlhelper.get_list('SELECT * FROM class WHERE id=%s LIMIT 1;',[student[2],])[0][1]
        return render(
            request,
            "edit_student.html",
            {
                'student':student,
                'class_name':class_name,
                'class_list':class_list,
                'class_name':class_name,
            }
        )
    if request.method =='POST':
        student_id =request.GET.get("nid")
        student_name =request.POST.get("student_name")
        class_id =request.POST.get("class_id")
        if sqlhelper.modify('UPDATE student SET name=%s,class_id=%s WHERE id =%s;',[student_name,class_id,student_id,]):
            return redirect('/student/')
        else:
            return redirect('/edit_student/?nid='+student_id)
        

