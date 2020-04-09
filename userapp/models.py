from django.db import models

# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=20,null=True)
    religious_name=models.CharField(max_length=20,null=True,blank=True)  #法名
    password=models.CharField(max_length=20,null=True)
    salt=models.CharField(max_length=20,null=True)
    danger=models.CharField(max_length=20,null=True)
    head_pic=models.ImageField(upload_to='pics',null=True)
    address=models.CharField(max_length=20,null=True)
    signature=models.CharField(max_length=30,null=True,blank=True)   #签名
    phone=models.CharField(max_length=20,null=True)
    qq=models.CharField(max_length=20,null=True)
    resever=models.CharField(max_length=20,null=True,blank=True)  #备用

