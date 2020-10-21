from django.db import models

# Create your models here.
class UserInfo(models.Model):
    nickname =models.CharField(max_length=32)
    username =models.CharField(max_length=32)
    password =models.CharField(max_length=64)
    gener_choices =(
        (1,'boy'),
        (2,'girl')
    )
    gender =models.IntegerField(choices=gener_choices)

class btoy(models.Model):
    '''
    g与b不能一样
    related_query_name 代表当需要反向查表时，related_query_name的值代表表名
    也就是当女生反向查表 a_set.all()
    男生：b_set.all()
    related_name 代表当需要反向查表时 related_name 的值代表表名
    而且不要_set了，直接是a.all() b.all()
    '''
    g =models.ForeignKey(to='UserInfo',related_name='g',on_delete=models.CASCADE)
    b =models.ForeignKey(to='UserInfo',related_name='b',on_delete=models.CASCADE)

class Comment(models.Model):

    news_id =models.IntegerField()
    content =models.CharField(max_length=32)
    user =models.CharField(max_length=32)
    '''
        关联自己的id，因为replayid只能是id存在的值
    '''
    replyid =models.ForeignKey('Comment',null=True,blank=True,related_name='reply',on_delete=models.CASCADE)


    '''
        新闻id  内容 用户   reply_id
    1    1      hh   root    null
    2    1      hh   root    null
    3    1      xx   shaowei null
    4    2      cc   root    null 
    5    1      nn   llll     2
    6    1      zz   xxxx     2
    7    1      ff   cccc     5
    '''
'''
新闻1    
    hh
    hh
        -nn
            -ff
        -zz
    shaowei
    root
新闻2
    cc
'''