from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import modbus_signal
from .serializers import modbus_signal_serializer


class MachineSignalViewSet(viewsets.ModelViewSet):
	queryset = modbus_signal.objects.all()
	serializer_class = modbus_signal_serializer
	filterset_fields = "__all__"

