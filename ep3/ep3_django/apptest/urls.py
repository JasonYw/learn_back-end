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
from django.urls import path,include
from apptest import views
from django.urls import re_path


urlpatterns = [
    path('class/',views.classes),
    path('add_class/',views.addclass),
    re_path(r'del_class/(\d+).html',views.del_class),
    re_path(r'edit_class/(\d+).html',views.edit_class),
    path('student/',views.student),
    path('add_student/',views.add_student),
    re_path(r'del_student/(\d+).html',views.del_student),
    re_path(r'edit_student/(\d+).html',views.edit_student),
    # path('test/',views.test),
]

