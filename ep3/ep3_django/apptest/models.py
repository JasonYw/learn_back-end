from django.db import models

# Create your models here.

class classes(models.Model):
    title =models.CharField(max_length=32)

class student(models.Model):
    name =models.CharField(max_length=64)
    class_id=models.ForeignKey('classes',null=True,on_delete=models.CASCADE)