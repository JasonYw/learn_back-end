import mysql.connector
from django.shortcuts import render
from django.shortcuts import redirect


def classes(request):
    connect =mysql.connector.connect(user="root",password="0125",database="django")
    cursor =connect.cursor()
    cursor.execute("SELECT id,title FROM class")
    class_list =cursor.fetchall()
    connect.close()
    print(class_list)
    return render(request,'class.html',{'class_list':class_list})

def add_class(request):
    if request.method =="GET":
        return render(request,'add_class.html')
    else:
        class_name =request.POST.get('title')
        connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute('INSERT IGNORE INTO class (title) VALUES (%s)',[class_name,])
        connect.commit()
        connect.close()
        return redirect('/class/')


