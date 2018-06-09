#coding=utf-8
from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from django.db.models import Max,F,Q

from .models import *
# Create your views here.

def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains = "八")
    list2=BookInfo.books1.all()
    max = list2.aggregate(Max('bpub_date'))
    #list3 =  list2.filter(bread__gt = F('bcomment'))
    #list3 = list2.filter(bread__lt = F('bcomment')*2)
    #list3 = list2.filter(isDelete=F('heroinfo__isDelete'))
    list3 = list2.filter(Q(pk__lt =3)|Q(bcomment__gt=10))
    content = {"list":list3,"max":max}
    return render(request, "booktest/index.html", content)

def area(request):
    area = AreaInfo.objects.get(pk=130100)
    content = {'area':area}
    return render(request, "booktest/area.html", content)
    # Area now:石家庄市
    # Parent Area:河北省
    # Son area:
    # 市辖区
    # 井陉县
    # 正定县
    # 栾城县
    # 行唐县
    # 灵寿县
    # 高邑县
    # 深泽县
    # 赞皇县dddd
    # 无极县
    # 平山县
    # 元氏县
    # 赵县
    # 辛集市
    # 藁城市
    # 晋州市
    # 新乐市
    # 鹿泉市




