# -*- coding: euckr -*-
# coding=utf-8

from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # Class-based views
    # URL /bookmark/��û�� ó���� �� Ŭ������ BookmarkLV�� ����, URL ������ �̸��� 'index'�� ���
    url(r'^$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/���� ��û�� ó���� �� Ŭ������ BookmarkDV�� ����, URL ������ �̸��� 'detail'�� ���
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail')
]