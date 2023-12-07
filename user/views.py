from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import UserSerializer
from utils.auth import JwtQueryParamsAuthentication


class UserInfoView(APIView):
	def get(self, request):
		token = request.META.get('HTTP_AUTHORIZATION')
		user = JwtQueryParamsAuthentication.authenticate(self,request)
		if user:
			return Response({'status':200,'results':user})
		else:
			return Response({'status':201,'results':"用户未登录"})

