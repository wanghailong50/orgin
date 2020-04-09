from django.db import models

# Create your models here.


class Slides(models.Model):
    title=models.CharField(max_length=20,null=True)
    loaddata=models.DateField(blank=True,auto_now_add=True,null=True)
    isshow=models.CharField(max_length=20)
    pic=models.ImageField(upload_to="pics",blank=True, null=True)


