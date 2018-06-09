#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import *
# Create your views here.


def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
#获取链接
def getTest1(request):
    return render(request, 'booktest/getTest1.html')
#一键一值
def getTest2(request):
    #根据键接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    #构造上下文
    context = {'a':a1,'b':b1,'c':c1}
    #向模板中传递上下文，并进行渲染
    return render(request, 'booktest/getTest2.html', context)

#一键多值
def getTest3(request):
    a1 = request.GET.getlist('a')
    context = {'a':a1}
    return render(request, 'booktest/getTest3.html', context)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request, 'booktest/postTest2.html', context)

def cookieTest(request):
    response  = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    #response.set_cookie("t1",'abc') 浏览器会把这个键值对保存，并在请求头中带上
    return response

#重定向网页，相当于浏览器重新向新的http请求
def redirectTest1(request):
    return HttpResponseRedirect('/booktest/redirectTest2/')

def redirectTest2(request):
    return HttpResponse('This is a redirect html file')

def session1(request):
    uname = request.session.get('myname', '未登录')    #退出显示未登录
    context = {'uname':uname}
    return render(request, 'booktest/session1.html', context)

    def session2(request):
        # 表单输入用户名
        return render(request,'booktest/session2.html')

    def session2_handle(request):
        #获取用户名，并保存在session中，重定向到登陆页面
        uname = request.POST['uname']
        request.session['myname'] = uname
        request.session.set_expiry(0)
        return redirect('/booktest/session1/')

def session3(request):
    #如果退出，则显示未登录
    del request.session['myname']
    return redirect('/booktest/session1/')

def index(request):
    return render(request, 'booktest/index.html')

def login(request):
    return render(request, 'booktest/login.html')

def login_handle(request):
    username = request.POST['uname']
    userpwd = request.POST['upwd']
    try:
        user = UserInfo.userObject.get(uname=username)
        if user.upwd == userpwd:
            info = '成功登陆'
            context = {'info':info}
            return render(request, 'booktest/login_handle.html', context)
        else:
            info = '密码错误'
            context = {'info': info}
            return render(request, 'booktest/login_handle.html',context)
    except:
        info = '用户名不存在'
        context = {'info': info}
        return render(request, 'booktest/login_handle.html', context)

def register(request):
    return render(request, 'booktest/register.html')

def register_handle(request):
    user = request.POST['uname']
    pwd = request.POST['upwd']

    tmpuser = UserInfo.userObject.filter(uname=user)
    if tmpuser.exists():    
        info = '用户名已经存在'
        context = {'info': info}
        return render(request, 'booktest/login_handle.html', context)
    else:
        if (len(user) > 10) or (len(pwd) > 10):
            info = '用户名或者密码过长，请重新输入'
            context = {'info': info}
            return render(request, 'booktest/login_handle.html', context)
        else:
            print("---------")
            print(user)
            print(pwd)
            newuser = UserInfo.userObject.create(user,pwd)
            newuser.save()
            info = '创建成功'
            context = {'info': info}
            return render(request, 'booktest/login_handle.html', context)

def exit(request):
    return redirect('/booktest/index/')









