"""drf-tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
	TokenVerifyView,
	token_obtain_pair
)
from user import views

urlpatterns = [
		path("admin/", admin.site.urls),
		path("", include_docs_urls(title = "DRF API文档", description = "Django REST framework")),
		# DRF 提供的一系列身份认证的接口，用于在页面中认证身份，详情查阅DRF文档
		path('api/auth/', include('rest_framework.urls', namespace = 'rest_framework')),
		# 获取Token的接口
		path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
		# 刷新Token有效期的接口
		path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
		# 验证Token的有效性
		path('api/token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),

		path('login/', TokenObtainPairView.as_view(), name = "登录"),

		path("pm/", include("pm.urls")),
		path("machine/", include("machine.urls")),
		re_path(r"userinfo/", views.UserInfoView.as_view())

]
