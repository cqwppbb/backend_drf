from django.db import models

# Create your models here.

class modbus_signal(models.Model):
    area = models.CharField(max_length=32)
    station = models.CharField(max_length=32)
    item = models.CharField(max_length=256)
    ip = models.CharField(max_length=64)
    address = models.IntegerField()
    ctime = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "设备测点"
        verbose_name_plural = verbose_name
