#coding=utf-8
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^index/$',views.index),
    #url(r'^(\d+)/(\d+)/(\d+)$',views.detail),#位置参数 
    url(r'^(?P<p3>\d+)/(?P<p1>\d+)/(?P<p2>\d+)$', views.detail), # 关键字参数
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),
    url(r'^postTest1/$', views.postTest1),
    url(r'^postTest2/$', views.postTest2),
    url(r'cookieTest/$',views.cookieTest),
    url(r'redirectTest1/$', views.redirectTest1),
    url(r'redirectTest2/$', views.redirectTest2),
    url(r'session1/$', views.session1),
    url(r'session2/$', views.session2),
    url(r'session3/$', views.session3),
    url(r'session2_handle/$', views.session2_handle),

    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^exit/$', views.exit),
    url(r'^login_handle/$', views.login_handle),
    url(r'^register_handle/$', views.register_handle),

]