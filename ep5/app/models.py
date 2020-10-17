from django.db import models

# Create your models here.
class UserType(models.Model):
    '''
    用户类型
    '''
    title =models.CharField(max_length=32)
    fo =models.ForeignKey('Foo',null=True,on_delete=models.CASCADE)

class UserInfo(models.Model):
    '''
        名字 
    '''
    name =models.CharField(max_length=16)
    age =models.IntegerField()
    ut =models.ForeignKey('UserType',null=True,on_delete=models.CASCADE)
    gt =models.ForeignKey('group',null=True,on_delete=models.CASCADE)


    def __str__(self):
        return "%s-%s" %(self.id,self.name)

class Foo(models.Model):
    caption =models.CharField(max_length=16)

class Group(models.Model):
    caption =models.CharField(max_length=32)

#==========================================
class Boy(models.Model):
    name =models.CharField(max_length=32)
    m =models.ManyToManyField('Girl',through="love",through_fields=('b','g')) #也可以写在Girl表中，并且不会往boy里添加任何列，会新建一个表表名为app_boy_m
    #会新建一个表表名为app_boy_m,表明里有三个列，id，boy_id,girl_id
    #无法直接对第三张表进行操作，间接对m操作
    #若自定义了love表l，又保留了ManyToMany，则django会建立四张表，boy girl love 以及app_boy_m
    #为了避免上述情况发生，给ManyTomany方法加入一个through告诉django 通过自定义的love来创建第三张表
    #through 通过love来联，throungh_fields 通过b和g来做关联列
    

class Girl(models.Model):
    name =models.CharField(max_length=32)
    #m =models.ManyToManyField('Boy')

class love(models.Model):  #->>此表可以自动生成
    b =models.ForeignKey('Boy',on_delete=models.CASCADE)
    g =models.ForeignKey('Girl',on_delete=models.CASCADE)

    class Meta: #联合索引
        unique_together=[
            ('b','g')
        ]






