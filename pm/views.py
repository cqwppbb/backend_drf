from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import machine_data, pm_data, pm_push, pm_finish_record, pm_modify_record
from .serializers import machine_data_serializer, pm_data_serializer, pm_push_serializer, pm_finish_record_serializer, \
	pm_modify_record_serializer
from utils.pagination import MyPageNumberPagination

class MachineDataViewSet(viewsets.ModelViewSet):
	queryset = machine_data.objects.all()
	serializer_class = machine_data_serializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	filterset_fields = "__all__"
	search_fields = "__all__"
	pagination_class = MyPageNumberPagination





class PmPushViewSet(viewsets.ModelViewSet):
	queryset = pm_push.objects.all()
	serializer_class = pm_push_serializer
	ffilter_backends = (DjangoFilterBackend, filters.SearchFilter)
	filterset_fields = "__all__"
	search_fields = "__all__"
	pagination_class = MyPageNumberPagination


class PmFinishRecordViewSet(viewsets.ModelViewSet):
	queryset = pm_finish_record.objects.all()
	serializer_class = pm_finish_record_serializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	filterset_fields = "__all__"
	search_fields = "__all__"
	pagination_class = MyPageNumberPagination

class PmDataViewSet(viewsets.ModelViewSet):
	queryset = pm_data.objects.all()
	serializer_class = pm_data_serializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	filterset_fields = "__all__"
	search_fields = "__all__"
	pagination_class = MyPageNumberPagination
	@action(methods = ['post'],detail=False)
	def add(self,request,*args,**kwargs):
		data = request.data
		range = data.get('range')
		del data['range']
		SaveData = pm_data_serializer(data = data)
		if not SaveData.is_valid():
			return Response(pm_data_serializer.errors)
		SaveData.save()
		return Response(data = SaveData.data,status = status.HTTP_200_OK)
	@action(methods = ['put'], detail = False)
	def edit (self, request):
		data = request.data
		range = data.pop('range')
		if range == 'all':
			obj = pm_data.objects.filter(item=data.get('item'))
		else:
			obj = pm_data.objects.filter(id=data.get('id'))
		s = pm_data_serializer(instance = obj, data = data)
		for i in obj:
			s = pm_data_serializer(instance = i,data = data)
			if not s.is_valid():
				return Response({"status": status.HTTP_400_BAD_REQUEST})
			s.save()
		return Response(data=s.data,status = status.HTTP_200_OK)


class PmModifyRecordViewSet(viewsets.ModelViewSet):
	queryset = pm_modify_record.objects.all()
	serializer_class = pm_modify_record_serializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	filterset_fields = "__all__"
	search_fields = "__all__"
	pagination_class = MyPageNumberPagination

	@action(methods = ['post'], detail = False)
	def add (self, request, *args, **kwargs):
		data = request.data
		range = data.get('range')
		del data['range']
		SaveData = pm_modify_record_serializer(data = data)
		if not SaveData.is_valid():
			return Response(status.HTTP_400_BAD_REQUEST)
		SaveData.save()
		response ={"data": SaveData.data,"code":200}
		return Response(response,status = status.HTTP_200_OK)

