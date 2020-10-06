# -*-coding:utf-8 -*-

"""ep4_django URL Configuration

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
from django.urls import re_path
from app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('app01/',include('app01.urls')),
    # re_path(r'index/(?P<a1>\d+)',views.index,name="n1"),
    path('login/',views.login,name="m1"),
    path('index/',views.index,name='n1'),
    re_path('edit/(\w+)/', views.edit,name='n2'),
    path(r'orm/',views.orm),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', views.index),
#     # path('edit/', views.edit),
#     re_path(r'edit/(\w+)/(\w+)/',views.edit),
# ]
