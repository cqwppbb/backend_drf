#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/11/23 14:07

from  django.contrib.auth.models import User
from  rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
