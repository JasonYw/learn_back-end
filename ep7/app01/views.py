from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.




def test(request):
    '''
    g =models.ForeignKey(to='UserInfo',related_name='a',on_delete=models.CASCADE)
    b =models.ForeignKey(to='UserInfo',related_name='b',on_delete=models.CASCADE)
    '''
    # b =models.UserInfo.objects.filter(gender=1,id=2).first()
    # g =models.UserInfo.objects.filter(gender=2,id=3).first()
    #models.btoy.objects.create(b_id =1,g_id=4)
    #models.btoy.objects.create(b=b,g=g) #fk 可以传对象 本质也是传id
    tom =models.UserInfo.objects.filter(id=1).first() #->userinfo对象
    for i in tom.b.all(): #关系表对象列表
        print (i.g.nickname) #g代表的女孩表
    return HttpResponse('200')

def test_m(request):
    print('200')
    return HttpResponse('200')