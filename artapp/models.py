from django.db import models

# Create your models here.

class Art(models.Model):
    title=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    loaddata = models.DateField(blank=True, auto_now_add=True, null=True)
    showdata=models.DateField(blank=True,auto_now_add=True,null=True)
    img=models.ImageField(upload_to="pic",null=True)
    text=models.TextField()
    resever=models.CharField(max_length=20,null=True)