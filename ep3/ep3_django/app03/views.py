from django.shortcuts import render
from django.shortcuts import redirect
from utils import sqlhelper

def index_(request):
    if request.GET.get("href") =='class':
        return redirect('/class/')
    elif request.GET.get("href") == 'teacher':
        return redirect('/teacher/')
    elif request.GET.get("href") == 'student':
        return redirect('/student/')
    else:
        return render(request,'index.html')

def classes(request):
    class_list =sqlhelper.get_list("SELECT id,title FROM class")
    return render(request,'class.html',{'class_list':class_list})

def add_class(request):
    if request.method =="GET":
        return render(request,'add_class.html')
    else:
        class_name =request.POST.get('title')
        class_num =sqlhelper.get_list('SELECT id FROM class ORDER BY id DESC LIMIT 1')
        if class_num ==[]:
            class_id =1
        else:
            class_id =class_num[0][0]+1
        sqlhelper.modify('INSERT IGNORE INTO class (id,title) VALUES (%s,%s)',[class_id,class_name,])
        return redirect('/class/')

def del_class(request):
    class_id =request.GET.get("nid")
    if sqlhelper.modify("DELETE FROM class WHERE id =%s",[class_id,]):
        return redirect('/class/')
    else:
        return redirect('/class/')

def edit_class(request):
    if request.method == "GET":
        class_id =request.GET.get("nid")
        class_title =sqlhelper.get_list('SELECT title FROM class WHERE id =%s LIMIT 1',[class_id])
        return render(request,'edit_class.html',{'result':[class_id,class_title[0][0]]})
    if request.method == "POST":
        class_id =request.GET.get("nid")
        class_title =request.POST.get("class_title")
        if class_title =='':
            return redirect('/del_class/?nid='+class_id)
        sqlhelper.modify("UPDATE class SET title=%s WHERE id=%s",[class_title,class_id])
        return redirect('/class/')
 
def teacher(request):
    teacher_list =sqlhelper.get_list('SELECT * FROM teacher')
    return render(request,'teacher.html',{'teacher_list':teacher_list})

def add_teacher(request):
    if request.method =="GET":
        return render(request,'add_teacher.html')
    if request.method =="POST":
        teacher_name =request.POST.get("teacher_name")
        teacher_id =sqlhelper.get_list('SELECT id FROM teacher ORDER BY id DESC LIMIT 1')
        if teacher_id ==[]:
            teacher_id =1
        else:
            teacher_id =teacher_id[0][0] +1
        sqlhelper.modify("INSERT INTO teacher (id,name) VALUES (%s,%s)",[teacher_id,teacher_name])
        return redirect('/teacher/')

def del_teacher(request):
    teacher_id =request.GET.get('nid')
    sqlhelper.modify('DELETE FROM teacher WHERE id=%s',[teacher_id,])
    return redirect('/teacher/')

def edit_teacher(request):
    if request.method =='GET':
        teacher_id =request.GET.get("nid")
        teacher_name =sqlhelper.get_list('SELECT * FROM teacher WHERE id =%s LIMIT 1',[teacher_id])
        return render(request,'edit_teacher.html',{'teacher_id':teacher_id,'teacher_name':teacher_name[0][1]})
    if request.method == 'POST':
        teacher_id =request.GET.get("nid")
        teacher_name =request.POST.get("teacher_name")
        sqlhelper.modify('UPDATE teacher SET name=%s WHERE id =%s',[teacher_name,teacher_id])
        return redirect('/teacher/')

def student(request):
    student_list =sqlhelper.get_list('SELECT s.id,s.name,c.title class FROM student s LEFT OUTER JOIN class c ON s.class_id =c.id')
    return render(request,"student.html",{'student_list':student_list})


def add_student(request):
    if request.method =="GET":
        class_list =sqlhelper.get_list('SELECT * FROM class')
        return render(request,"add_student.html",{'class_list':class_list})
    if request.method =="POST":
        class_id =request.POST.get("class_id")
        if len(class_id) >0:
            student_name =request.POST.get("student_name")
            student_id =sqlhelper.get_list('SELECT id FROM student ORDER BY id DESC LIMIT 1')
            if student_id == []:
                student_id = 1
            else:
                student_id = student_id[0][0]+1
            sqlhelper.modify('INSERT INTO student (id,name,class_id) VALUES (%s,%s,%s)',[student_id,student_name,class_id])
            return redirect('/student/')
        else:
            return render(request,"add_student.html")

def del_student(request):
    student_id = request.GET.get("nid")
    sqlhelper.modify("DELETE FROM student WHERE id=%s",[student_id])
    return redirect('/student/')


def edit_student(request):
    if request.method == 'GET':
        class_list =sqlhelper.get_list('SELECT * FROM class')
        student_id =request.GET.get("nid")
        student =sqlhelper.get_list('SELECT * FROM student WHERE id=%s LIMIT 1',[student_id,])[0]
        class_name =sqlhelper.get_list('SELECT * FROM class WHERE id=%s LIMIT 1 ',[student[2],])[0][1]
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
        if sqlhelper.modify('UPDATE student SET name=%s,class_id=%s WHERE id =%s',[student_name,class_id,student_id,]):
            return redirect('/student/')
        else:
            return redirect('/edit_student/?nid='+student_id)
        

