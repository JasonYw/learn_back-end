from django.urls import path
from django.urls import re_path
from app import views
urlpatterns = [
    re_path(r'index.html$',views.index),
    path(r'index/',views.index),
]

