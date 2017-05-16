# -*- coding: euckr -*-
# coding=utf-8

from django.conf.urls import url
# URLconf에서 뷰를 호출하므로, 뷰 모듈의 모든 클래스를 임포트함 뷰 클래스가 많은 경우 이렇게 한 번에 임포트하면 편리함.
from blog.views import *

urlpatterns = [

    # 정규 표현식은 가독성이 떨어지므로 주석으로 예시 URL을 기록하면 이해하기 쉬움.
    # Example: /
    # URL /blog/ 요청을 처리할 뷰 클래스를 PostLV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:index'
    url(r'^$', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    # URL /blog/post/ 요청을 처리할 뷰 클래스를 PostLV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_list'
    # PostLV 뷰 클래스는 /blog/와 /blog/post/ 2가지 요청을 모두 처리한다는 점을 유의!
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    # URL /blog/post/영단어/ 요청을 처리할 뷰 클래스를 PostDV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_detail'
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    # URL /blog/archive/ 요청을 처리할 뷰 클래스를 PostAV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_archive'
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    # URL /blog/4자리 숫자/ 요청을 처리할 뷰 클래스를 PostYAV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_year_archive'
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    # URL /blog/4자리 숫자/3자리 소문자/ 요청을 처리할 뷰 클래스를 PostMAV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_month_archive'
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    # URL /blog/4자리 숫자/3자리 소문자/2자리 숫자/ 요청을 처리할 뷰 클래스를 PostYAV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_day_archive'
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    # URL /blog/today/ 요청을 처리할 뷰 클래스를 PostYAV로 지정, URL 패턴의 이름은 이름공간을 포함해 'blog:post_today_archive'
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
]