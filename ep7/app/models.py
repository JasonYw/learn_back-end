from django.db import models

# Create your models here.
class Boy(models.Model):
    name =models.CharField(max_length=32)
    username =models.CharField(max_length=32)
    password =models.CharField(max_length=32)

class Girl(models.Model):
    name =models.CharField(max_length=32)
    username =models.CharField(max_length=32)
    password =models.CharField(max_length=32)

class Link_by(models.Model):
    boy_id =models.ForeignKey('Boy',on_delete=models.CASCADE)
    girl_id =models.ForeignKey('Girl',on_delete=models.CASCADE)
    

