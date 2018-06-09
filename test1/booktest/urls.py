from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index),   #after match the project urls.py urls then,match there
    url(r'^(\d+)$', views.show)
]