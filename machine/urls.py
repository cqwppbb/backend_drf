#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/11/24 10:16

from django.urls import path,include
from rest_framework.routers import DefaultRouter

from machine import views

router = DefaultRouter()
router.register(prefix = "machinesignal",viewset = views.MachineSignalViewSet)


urlpatterns = [
		path('',include(router.urls)),
]
