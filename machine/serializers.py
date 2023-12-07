#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/11/23 14:07

from  django.contrib.auth.models import User
from  rest_framework import serializers

from .models import modbus_signal


class modbus_signal_serializer(serializers.ModelSerializer):
	class Meta:
		model = modbus_signal
		fields = '__all__'

