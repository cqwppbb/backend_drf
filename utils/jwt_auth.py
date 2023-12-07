#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author  : CQW
# @time    : 2023/12/7 12:32

import jwt
import datetime
from django.conf import settings

def create_token(payload,timeout=1):
	salt = settings.SECRET_KEY

	headers = {
			'typ':'jwt',
			'alg':'HS256',
	}

	payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes = timeout)
	token = jwt.encode(headers = headers, payload = payload, key = salt, algorithm = "HS256").decode("utf-8")

	return token
