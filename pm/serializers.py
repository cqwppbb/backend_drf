#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/11/23 14:07

from  rest_framework import serializers

from .models import machine_data,pm_data,pm_push,pm_finish_record,pm_modify_record


class machine_data_serializer(serializers.ModelSerializer):
	class Meta:
		model = machine_data
		fields = '__all__'

class pm_data_serializer(serializers.ModelSerializer):
	class Meta:
		model = pm_data
		fields = '__all__'

class pm_push_serializer(serializers.ModelSerializer):
	class Meta:
		model = pm_push
		fields = '__all__'

class pm_finish_record_serializer(serializers.ModelSerializer):
	class Meta:
		model = pm_finish_record
		fields = '__all__'

class pm_modify_record_serializer(serializers.ModelSerializer):
	class Meta:
		model = pm_modify_record
		fields = '__all__'
