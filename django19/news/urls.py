from django.conf.urls import url
from .views import (
news_create,
news_delete,
news_list,
news_detail,
news_update,
)
from django.contrib import admin

urlpatterns = [

    url(r'^create/$',news_create),
    url(r'^(?P<var>\d+)/$',news_detail,name='detail'),  # p<id>\d+ takes a variable named id ans send it to news_detail,d+ only digits
    url(r'^$', news_list,name='list'),
    url(r'^(?P<var>\d+)/edit/$',news_update,name='update'),
    url(r'^(?P<var>\d+)/delete/$',news_delete),
]
