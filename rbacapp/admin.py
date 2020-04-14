from django.contrib import admin
from rbacapp import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.Permission)
admin.site.register(models.Role)