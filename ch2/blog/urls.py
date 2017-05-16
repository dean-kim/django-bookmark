# -*- coding: euckr -*-
# coding=utf-8

from django.conf.urls import url
# URLconf���� �並 ȣ���ϹǷ�, �� ����� ��� Ŭ������ ����Ʈ�� �� Ŭ������ ���� ��� �̷��� �� ���� ����Ʈ�ϸ� ����.
from blog.views import *

urlpatterns = [

    # ���� ǥ������ �������� �������Ƿ� �ּ����� ���� URL�� ����ϸ� �����ϱ� ����.
    # Example: /
    # URL /blog/ ��û�� ó���� �� Ŭ������ PostLV�� ����, URL ������ �̸��� �̸������� ������ 'blog:index'
    url(r'^$', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    # URL /blog/post/ ��û�� ó���� �� Ŭ������ PostLV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_list'
    # PostLV �� Ŭ������ /blog/�� /blog/post/ 2���� ��û�� ��� ó���Ѵٴ� ���� ����!
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    # URL /blog/post/���ܾ�/ ��û�� ó���� �� Ŭ������ PostDV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_detail'
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    # URL /blog/archive/ ��û�� ó���� �� Ŭ������ PostAV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_archive'
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    # URL /blog/4�ڸ� ����/ ��û�� ó���� �� Ŭ������ PostYAV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_year_archive'
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    # URL /blog/4�ڸ� ����/3�ڸ� �ҹ���/ ��û�� ó���� �� Ŭ������ PostMAV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_month_archive'
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    # URL /blog/4�ڸ� ����/3�ڸ� �ҹ���/2�ڸ� ����/ ��û�� ó���� �� Ŭ������ PostYAV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_day_archive'
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    # URL /blog/today/ ��û�� ó���� �� Ŭ������ PostYAV�� ����, URL ������ �̸��� �̸������� ������ 'blog:post_today_archive'
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
]