import mysql.connector
from django.shortcuts import render
from django.shortcuts import redirect

def index_(request):
    return redirect('/class/')

def classes(request):
    connect =mysql.connector.connect(user="root",password="0125",database="django")
    cursor =connect.cursor()
    cursor.execute("SELECT id,title FROM class")
    class_list =cursor.fetchall()
    connect.close()
    return render(request,'class.html',{'class_list':class_list})

def add_class(request):
    if request.method =="GET":
        return render(request,'add_class.html')
    else:
        class_name =request.POST.get('title')
        connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute('SELECT id FROM class ORDER BY id DESC LIMIT 1')
        class_num =cursor.fetchall()
        if class_num ==[]:
            class_id =1
        else:
            class_id =class_num[0][0]+1
        cursor.execute('INSERT IGNORE INTO class (id,title) VALUES (%s,%s)',[class_id,class_name,])
        connect.commit()
        connect.close()
        return redirect('/class/')

def del_class(request):
    class_id =request.GET.get("nid")
    connect =mysql.connector.connect(user="root",password="0125",database="django")
    cursor =connect.cursor()
    cursor.execute("DELETE FROM class WHERE id =%s",[class_id,])
    connect.commit()
    connect.close()
    return redirect('/class/')

def edit_class(request):
    connect =mysql.connector.connect(user="root",password="0125",database="django")
    cursor =connect.cursor()
    if request.method == "GET":
        class_id =request.GET.get("nid")
        cursor.execute('SELECT title FROM class WHERE id =%s LIMIT 1',[class_id])
        class_title =cursor.fetchall()
        connect.close()
        return render(request,'edit_class.html',{'result':[class_id,class_title[0][0]]})
    if request.method == "POST":
        class_id =request.GET.get("nid")
        class_title =request.POST.get("class_title")
        if class_title =='':
            connect.close()
            return redirect('/del_class/?nid='+class_id)
        cursor.execute("UPDATE class SET title=%s WHERE id=%s",[class_title,class_id])
        connect.commit()
        connect.close()
        return redirect('/class/')
 