#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/12/7 10:56

from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from jwt import exceptions
from user.serializers import UserSerializer
from  django.contrib.auth.models import User


class JwtQueryParamsAuthentication(BaseAuthentication):

	def authenticate(self,request):
		AUTHORIZATION = request.META.get('HTTP_AUTHORIZATION')
		token = AUTHORIZATION.split(' ')[1]
		salt = settings.SECRET_KEY
		payload = None
		msg = None
		try:
			decoded_data = jwt.decode(str(token), salt, algorithms = ["HS256"])
		except exceptions.ExpiredSignatureError:
			msg = 'token已失效'
			raise AuthenticationFailed({'code':1003,'error':'token已失效'})
		except jwt.DecodeError:
			msg = 'token认证失败'
			raise AuthenticationFailed({'code': 1003, 'error': 'token认证失败'})
		except jwt.InvalidTokenError:
			msg = '非法的token'
			raise AuthenticationFailed({'code': 1003, 'error': '非法的token'})
		userId = decoded_data.get('user_id', None)
		qs = User.objects.get(id=userId)
		serializer = UserSerializer(qs)
		return serializer.data
