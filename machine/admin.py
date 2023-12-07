from django.contrib import admin
from machine import models

# Register your models here.

class modbus_signal_admin(admin.ModelAdmin):
    list_display = ('area','station','item','ip','address','ctime')
admin.site.register(models.modbus_signal,modbus_signal_admin)

admin.site.index_title = "测点数据"
