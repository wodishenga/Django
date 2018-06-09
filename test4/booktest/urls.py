from django.conf.urls import url
import views
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)$', views.show, name="show"),
    url(r'^index2$', views.index2,name='index2'),
    url(r'^user1$', views.user1,name='user1'),
    url(r'^htmlTest', views.htmlTest,name='htmlTest'),
    url(r'^crsf1/$', views.crsf1,name='crsf1'),
    url(r'^crsf2/$', views.crsf2,name='crsf2'),

]