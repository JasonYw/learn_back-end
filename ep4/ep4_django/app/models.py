from django.db import models

# Create your models here.
class Userinfo(models.Model):
    '''
        创建一行表
    '''
    #自增int
    #nid =models.AutoField()

    #自增长整型 primary_key=True设置主键
    #可以不写 django会自动创建一列名为id的主键 int 自增 主键 
    id =models.BigAutoField(primary_key=True)  

    #字符串类型 max_length最大长度为32 CharField必须指定max_length
    user=models.CharField(max_length=32)

    #字符串类型 max_length最大长度64
    password =models.CharField(max_length=64)

    #给旧数据库的时候，添加新列的时候
    # 要说明null=True ，也就是可以为空 或 default=1 添加默认值
    age =models.IntegerField(default=1) 

    #添加外键约束，但是要允许空值,在数据库里会生成 ug_id 存的是外键的id
    ug =models.ForeignKey('Usergroup',null=True,on_delete=models.CASCADE)


class Usergroup(models.Model):
    '''
        单表增加
        models.Usergroup.objects.create(title="销售部")

        筛选之后删除
        models.Usergroup.objects.filter(id=1).delete()

        筛选之后修改
        models.Usergroup.objects.filter(id=1).update(title='newvalue')

        #查
        group_list =models.Usergroup.objects.all() 查全部的
        group_list =models.Usergroup.objects.filter(id=1) 条件查询 若多个条件 则默认为and
        id__gt=1 表示 id>1 ,id__lt=1 表示id<1
        

    '''
    title =models.CharField(max_length=32)
