# coding:utf-8
# @author : CQW
# @time   : 2023/12/13 15:42
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
	page_size = 10  # default page size
	page_size_query_param = 'size'  # ?page=xx&size=??
	max_page_size = 200  # max page size
