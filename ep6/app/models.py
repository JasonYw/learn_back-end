from django.db import models


class Userinfo(models.Model):
    username =models.CharField(max_length=32)

    #以下
    #本质都是字符串
    #但是对这些列操作时，django会进行正则表达式的验证
    #只有验证通过之后才可以进行入库
    #但是在自己写的views中无法生效，只有在django-admin中才可以
    #在admin文件中注册userinfo
    #from app import models
    #admin.site.register(models.Userinfo)
    #可以在django-admin自带的后台管理中看到Userinfo,在django-admin自带的后台管理中就可以使用以下的列，并会进行正则检查
    email =models.EmailField(null=True,default='root@root.com',unique=True)#unique为唯一索引，default为默认值
    file =models.FileField(null=True) #用于上传文件
    ctime =models.DateTimeField(null=True)
    integer =models.IntegerField(null=True,db_index=True)#db_idnex为索引
    Decimaler =models.DecimalField(max_digits=30,decimal_places=10,null=True)#max_digit设置总长度，decimal_places设置小数的位数
    color_list =(
        (1,'black'),
        (2,'white'),
        (3,'blue'),
    )
    color =models.IntegerField(choices=color_list,null=True) #choices 代表可选择的 也就是这个列只有1，2，3能填入

    floater =models.FloatField(null=True,blank=True,verbose_name="age",editable=True,help_text='help you')
    #以下针对django-admin而言 
    #blank 是否可以为空ch
    #editable 是否可以编辑
    #verbose_name 在django-admin中的input中改名字
    #help_text 输入框的提示信息
    #error_messages 自定义错误信息，但是优先级较低，django-admin不会优先显示它
    




    # email =models.EmailField()
    # ip =models.IPAddressField()
    # slug =models.SlugField()
    # uuid =models.UUIDField()
    # filepath =models.FilePathField()
    # file =models.FieldFile()
    # image =models.ImageField()

    #联合索引
    # class Meta: 
        # unique_together=(#联合唯一索引
        #     ('email','c-time'),
        # )
        # index_together=(#联合不唯一索引
        #     ('email','c-time'),
        # )

# Create your models here.
