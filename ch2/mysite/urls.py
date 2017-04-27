# -*- coding: euckr -*-
# coding=utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# 장고의 내장함수인 url() 함수 import
from django.conf.urls import include, url
from django.contrib import admin

# URLconf에서 뷰를 호출하므로 뷰 모델의 관련 클래스를 import.
# from bookmark.views import BookmarkLV, BookmarkDV - APP_URLCONF 로 옮길 줄을 주석처리함.


# url() 함수는 다음과 같이 5개의 인자를 가지고 있음 앞의 2개는 필수인자 뒤 3개는 선택적 인자임
# url(regex, view, kwargs=None, name=None, prefix='')
urlpatterns = [
    # admin site 관련 URLconf가 정의
    # URLconf를 다른 곳에서 정의한 URLconf를 가져와서 재활용하고자 할 때는 include() 함수를 사용.
    # 다만 Admin site에 대한 URLconf인 admin.site.urls를 재활용할 때는 예외적으로 include()를 사용하지 않아도 가능
    # 다음의 2가지 모두 가능함.
    # url(r'^admin/', admin.site.urls)
    # url(r'^admin/', include(admin.site.urls))
    url(r'^admin/', admin.site.urls),

    # 북마크 앱의 APP_URLCONF를 포함하고 이름공간을 'bookmark'라고 지정
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # Class-based views for Bookmark app - 아래의 코드들은 APP_URLCONF 로 옮기므로 주석처리

    # 뷰를 클래스형 뷰로 정의하기 위해 각 URL에 따른 해당 클래스 및 as_view 메소드를 지정
    # URL /bookmark/요청을 처리할 뷰 클래스를 BookmarkLV로 지정, URL 패턴의 이름은 'index'로 명명
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/숫자 요청을 처리할 뷰 클래스를 BookmarkDV로 지정, URL 패턴의 이름은 'detail'로 명명
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
