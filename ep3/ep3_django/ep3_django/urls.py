"""ep3_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app03 import views
from app03 import modal_views


urlpatterns = [
    path('test/',views.test),
    path('layout/',views.layout),
    path('',views.login),
    path('index/',views.index_),
    path('modal_register/',modal_views.register),
    path('manage/',modal_views.self_manage),
    path('class/', views.classes),
    path("add_class/",views.add_class),
    path("del_class/",views.del_class),
    path("edit_class/",views.edit_class),
    path("teacher/",views.teacher),
    path("add_teacher/",views.add_teacher),
    path("del_teacher/",views.del_teacher),
    path("edit_teacher/",views.edit_teacher),
    path("student/",views.student),
    path("add_student/",views.add_student),
    path("del_student/",views.del_student),
    path("edit_student/",views.edit_student),
    path("modal_add_class/",modal_views.add_class),
    path("modal_del_class/",modal_views.del_class),
    path("modal_edit_class/",modal_views.edit_class),
    path("modal_add_student/",modal_views.add_student),
    path("modal_edit_student/",modal_views.edit_student),
    path("modal_del_student/",modal_views.del_student),
    path("modal_add_teacher/",modal_views.add_teacher),
    path("modal_del_teacher/",modal_views.del_teacher),
    path("modal_edit_teacher/",modal_views.edit_teacher),
    path("modal_add_1_teacher/",modal_views.add_1_teacehr),
]
