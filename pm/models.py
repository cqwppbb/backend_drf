from django.db import models


class machine_data(models.Model):
	area = models.CharField(max_length = 32)
	station = models.CharField(max_length = 32)
	item = models.CharField(max_length = 64)
	val = models.IntegerField()
	ctime = models.DateField(auto_now = True)

	class Meta:
		verbose_name = "PM设备数据"
		verbose_name_plural = verbose_name

	# def __str__ (self):
	# 	return self.station


class pm_data(models.Model):
	area = models.CharField(max_length = 32)
	machine = models.CharField(max_length = 32)
	station = models.CharField(max_length = 32)
	item = models.CharField(max_length = 64)
	detail = models.CharField(max_length = 256)
	frequency = models.IntegerField()
	type = models.CharField(max_length = 32)
	ctime = models.DateField(auto_now = True)

	class Meta:
		verbose_name = "PM内容"
		verbose_name_plural = verbose_name


class pm_push(models.Model):
	area = models.CharField(max_length = 32)
	machine = models.CharField(max_length = 32)
	station = models.CharField(max_length = 32)
	item = models.CharField(max_length = 64)
	detail = models.CharField(max_length = 256, default = "")
	frequency = models.IntegerField(default = 0)
	type = models.CharField(max_length = 32, default = "T")
	val_last = models.IntegerField(default = 0)
	val_current = models.IntegerField(default = 0)
	time_last = models.DateField()
	life = models.IntegerField(default = 0)
	push = models.IntegerField(default = 0)
	done = models.IntegerField(default = 0)
	ctime = models.DateField(auto_now = True)

	class Meta:
		verbose_name = "PM推送数据"
		verbose_name_plural = verbose_name


class pm_finish_record(models.Model):
	area = models.CharField(max_length = 32)
	machine = models.CharField(max_length = 32)
	station = models.CharField(max_length = 32)
	item = models.CharField(max_length = 64)
	detail = models.CharField(max_length = 256, default = "")
	frequency = models.IntegerField(default = 0)
	type = models.CharField(max_length = 32, default = "T")
	val_last = models.IntegerField(default = 0)
	val_current = models.IntegerField(default = 0)
	time_last = models.DateField()
	life = models.IntegerField(default = 0)
	push = models.IntegerField(default = 0)
	done = models.IntegerField(default = 0)
	user = models.CharField(max_length = 32)
	ctime = models.DateField(auto_now = True)

	class Meta:
		verbose_name = "PM完成记录"
		verbose_name_plural = verbose_name


class pm_modify_record(models.Model):
	area = models.CharField(max_length = 32)
	machine = models.CharField(max_length = 32)
	station = models.CharField(max_length = 32)
	item = models.CharField(max_length = 64)
	detail = models.CharField(max_length = 256)
	frequency = models.IntegerField()
	type = models.CharField(max_length = 32)
	user =models.CharField(max_length = 256)
	notes = models.CharField(max_length =256)
	ctime = models.DateField(auto_now = True)

	class Meta:
		verbose_name = "PM修改记录"
		verbose_name_plural = verbose_name
