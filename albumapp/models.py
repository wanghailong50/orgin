from django.db import models

# Create your models here.


class Album(models.Model):
    pic=models.ImageField(upload_to='pic1',blank=True,null=True)  #专辑图片
    name=models.CharField(max_length=20,null=True)
    setcion_number=models.CharField(max_length=20,null=True)
    publish=models.DateField(auto_now_add=True,null=True)


class Setcion(models.Model):
    setcion_name=models.CharField(max_length=20,null=True)
    video_size=models.CharField(max_length=20,null=True)
    video_time=models.CharField(max_length=20,null=True)
    video_address=models.CharField(max_length=50,null=True)
    album_id=models.ForeignKey(to='Album',blank=True,on_delete=models.CASCADE)
    ready=models.CharField(max_length=20,null=True)

