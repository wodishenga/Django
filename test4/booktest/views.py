#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def index(request):
    list = HeroInfo.objects.all()
    content = {'list':list}
    return render(request, 'booktest/index.html', content)

#反向解析
def show(request, id):
    content = {'id':id}
    return render(request, 'booktest/show.html', content)

#模板继承
def index2(request):
    return render(request, 'booktest/index2.html')

def user1(request):
    context = {"text":"xixi"}
    return render(request, 'booktest/user1.html', context)

#html转义
def htmlTest(request):
    context = {'t1':'<h1>abc<h1>','t2':"xixi"}
    return render(request, 'booktest/htmlTest.html', context)

#csrf
def crsf1(request):
    return render(request, 'booktest/crsf1.html')

def crsf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

