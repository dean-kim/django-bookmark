# -*- coding: euckr -*-
# coding=utf-8

from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # Class-based views
    # URL /bookmark/요청을 처리할 뷰 클래스를 BookmarkLV로 지정, URL 패턴의 이름은 'index'로 명명
    url(r'^$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/숫자 요청을 처리할 뷰 클래스를 BookmarkDV로 지정, URL 패턴의 이름은 'detail'로 명명
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')
]