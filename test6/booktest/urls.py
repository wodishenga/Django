from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pro/$', views.pro),
    url(r'^city(\d+)/$', views.city),
    url(r'^htmlEditor/$', views.htmlEditor),
    url(r'^content/$', views.htmlHandle),
    url(r'^cache_test/$',views.cache_test),
]

