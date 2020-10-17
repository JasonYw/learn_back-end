from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app import models


def test(request):
    #python .\manage.py createsuperuser 创建django超级用户
    models.Userinfo.objects.create(username="root",email="qqqqqq")
    models.Userinfo.objects.create(username="root",email="qqqqqq",ctime='2011-01-01')
    return HttpResponse('200')


# Create your views here.
