#coding=utf-8
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.conf import settings
from django.core.paginator import Paginator
import os

def index(request):
    return render(request, 'booktest/index.html')

#中间件
def MyExp(request):
    a = int('abc')
    return HttpResponse('haha')

def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')

def uploadHandle(request):
    if request.method == 'POST':
        pic =  request.FILES['pic']
        picUpload = os.path.join(settings.MEDIA_ROOT, pic.name)
        with open(picUpload, 'w') as f:
            for c in pic.chunks():
                f.write(c)
        return HttpResponse('<img src="/static/media/%s" />'%pic.name)
    else:
        return HttpResponse('error')

#分页
def herolist(request,index):
    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)
    if index == "":
        index = 1
    page = paginator.page(index)
    context = {"page":page}
    return render(request, "booktest/herolist.html", context)

#ajax

def area(request):
    return render(request, 'booktest/areainfo.html')

def area2(request, id):
    id1 = int(id)
    if (id1 == 0):
        data = AreaInfo.objects.filter(aParent__isnull=True)
    else:
        data = [{}]
    list = []
    for area in data:
        list.append([area.id, area.atitle])
    return JsonResponse({'data':list})  #注意这里一定要搞成json格式