# -*- coding: euckr -*-
# coding=utf-8

from django.conf.urls import url
from bookmark.views import *

urlpatterns = [
    # Class-based views
    # URL /bookmark/요청을 처리할 뷰 클래스를 BookmarkLV로 지정, URL 패턴의 이름은 'index'로 명명
    url(r'^$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/숫자 요청을 처리할 뷰 클래스를 BookmarkDV로 지정, URL 패턴의 이름은 'detail'로 명명
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    # Example: /add/
    url(r'^add/$', BookmarkCreateView.as_view(), name='add'),

    # Example: /change
    url(r'^change/$', BookmarkChangeLV.as_view(), name='change'),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name='update'),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name='delete'),
]