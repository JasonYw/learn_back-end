from django.db import models

# Create your models here.
class UserType(models.Model):
    '''
    用户类型
    '''
    title =models.CharField(max_length=32)

class UserInfo(models.Model):
    '''
        名字 
    '''
    name =models.CharField(max_length=16)
    age =models.IntegerField()
    ut =models.ForeignKey('UserType')