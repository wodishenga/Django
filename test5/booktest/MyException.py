#coding=utf-8
from django.http import HttpResponse

class MyException():
    """视图中出现异常会调到这里"""
    def process_exception(request, response, exception):
            return  HttpResponse(exception.message) #返回异常信息

