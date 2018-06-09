#coding=utf-8
from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from models import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')

#获取省信息
def pro(request):
    #[{},{}]
    data = AreaInfo.objects.filter(aParent__isnull=True)
    list = []
    for area in data:
        list.append([area.id, area.atitle])
    return JsonResponse({'data':list})

def city(request, id):
    data = AreaInfo.objects.filter(aParent_id=id)
    #[{},{}]
    list = []
    for area in data:
        list.append({'id':area.id, 'atitle':area.atitle})
    return JsonResponse({'data': list})

#自定义编辑器
def htmlEditor(request):
    return render(request, 'booktest/htmlEditor.html')

def htmlHandle(request):
    html = request.POST['hcontent']

    test = Test()
    test.content = html
    test.save()
    context = {"data":html}
    return render(request, 'booktest/htmlShow.html',context)

#@cache_page(60*15)     1.用装饰器实现缓存
def cache_test(request):
    #djongo会先到缓存中找，如果缓存中有则返回缓存中的数据，没有才返回现有的数据
    #so这里如果修改hello,xiaozhu，该视图还是会返回hello,xiaozhu
    #return  HttpResponse('hello,xiaozhu')
    #2. 用api实现缓存    手动设置保存到redis数据库中
    cache.set('key1','value1',600)
    print(cache.get('key1'))
    cache.clear()       #清空全部缓存
    return render(request, 'booktest/cache_test.html')








