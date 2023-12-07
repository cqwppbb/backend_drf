#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/11/24 10:16

from django.urls import path,include
from rest_framework.routers import DefaultRouter

from pm import views

router = DefaultRouter()

router.register("machinedata",viewset = views.MachineDataViewSet)
router.register("pmdata",views.PmDataViewSet)
router.register("pmpush",views.PmPushViewSet)
router.register("pmfinishrecord",views.PmFinishRecordViewSet)
router.register("pmmodifyrecord",views.PmModifyRecordViewSet)

urlpatterns = [
		path('',include(router.urls)),
]
