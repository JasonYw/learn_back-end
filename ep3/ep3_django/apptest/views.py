from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import  redirect
from apptest import models


def test(request):
    models.classes.objects.create(title="class1")
    models.classes.objects.create(title="class2")
    return HttpResponse('200')
# Create your views here.
def classes(request):
    class_list_1 =models.classes.objects.all()
    class_list =[]
    for i in class_list_1:
        class_list.append((i.id,i.title))
    return render(request,'class.html',{'class_list':class_list})

def addclass(request):
    if request.method =='GET':
        return render(request,'add_class.html')
    if request.method =='POST':
        title =request.POST.get('title')
        models.classes.objects.create(title=title)
        return redirect('/test/class/')

def del_class(request,nid):
    print(nid)
    models.classes.objects.filter(id=nid).delete()
    return redirect('/test/class/')

def edit_class(request,nid):
    if request.method =='GET':
        class_data =models.classes.objects.filter(id=nid)
        class_tupe =(class_data[0].id,class_data[0].title)
        return render(request,'edit_class.html',{'result':class_tupe})
    else:
        class_name =request.POST.get("class_title")
        if class_name == '':
            return render(request,'edit_class.html',{'error':'empty input'})
        models.classes.objects.filter(id=nid).update(title=class_name)
        return redirect('/test/class/')

def student(request):
    if request.method == "GET":
        student_list_1 =models.student.objects.all()
        student_list =[]
        for i in student_list_1:
            student_list.append((i.id,i.name,i.class_id_id))
        return render(request,'student.html',{'student_list':student_list})
    
def add_student(request):
    if request.method =="GET":
        class_list_1 =models.classes.objects.all()
        class_list =[]
        for i in class_list_1:
            class_list.append((i.id,i.title))
        return render(request,'add_student.html',{'class_list':class_list})
    else:
        class_id =request.POST.get("class_id")
        stu_name =request.POST.get("student_name")
        if stu_name =="":
            return redirect('/test/add_student/')
        models.student.objects.create(name=stu_name,class_id_id=int(class_id))
        return redirect('/test/student/')
    
def del_student(requset,nid):
    models.student.objects.filter(id=nid).delete()
    return redirect('/test/student/')    

def edit_student(request,nid):
    if request.method =="GET":
        class_list_1 =models.classes.objects.all()
       
        student_ =models.student.objects.filter(id=nid)
        student =(student_[0].id,student_[0].name,student_[0].class_id)
        class_list =[]
        for i in class_list_1:
            class_list.append((i.id,i.title))
        return render(request,'edit_student.html',{'student':student,'class_list':class_list})
    else:
        stu_name =request.POST.get("student_name")
        stu_class =request.POST.get("class_id")
        if stu_name =='':
            return redirect('/test/edit_student/'+nid+'.html')
        models.student.objects.filter(id=nid).update(name=stu_name,class_id_id=stu_class) 
        return redirect('/test/student/')   
