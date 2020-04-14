from django.db import models

# Create your models here.


class Permission(models.Model):
    title=models.CharField(max_length=20,verbose_name='标题')
    url=models.CharField(max_length=128,verbose_name='url')
    is_menu=models.BooleanField(default=False,verbose_name='是否为菜单')


class Role(models.Model):
    title=models.CharField(max_length=20,verbose_name='角色名称')
    permissions=models.ManyToManyField(to='Permission',blank=True,verbose_name='角色拥有的权限')


class UserInfo(models.Model):
    name=models.CharField(max_length=20,verbose_name='用户名')
    password=models.CharField(max_length=20,verbose_name='用户名密码')
    roles=models.ManyToManyField(to='Role',blank=True,verbose_name='拥有的所有角色')