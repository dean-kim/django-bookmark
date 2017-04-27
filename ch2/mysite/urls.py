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
# ����� �����Լ��� url() �Լ� import
from django.conf.urls import include, url
from django.contrib import admin

# URLconf���� �並 ȣ���ϹǷ� �� ���� ���� Ŭ������ import.
# from bookmark.views import BookmarkLV, BookmarkDV - APP_URLCONF �� �ű� ���� �ּ�ó����.


# url() �Լ��� ������ ���� 5���� ���ڸ� ������ ���� ���� 2���� �ʼ����� �� 3���� ������ ������
# url(regex, view, kwargs=None, name=None, prefix='')
urlpatterns = [
    # admin site ���� URLconf�� ����
    # URLconf�� �ٸ� ������ ������ URLconf�� �����ͼ� ��Ȱ���ϰ��� �� ���� include() �Լ��� ���.
    # �ٸ� Admin site�� ���� URLconf�� admin.site.urls�� ��Ȱ���� ���� ���������� include()�� ������� �ʾƵ� ����
    # ������ 2���� ��� ������.
    # url(r'^admin/', admin.site.urls)
    # url(r'^admin/', include(admin.site.urls))
    url(r'^admin/', admin.site.urls),

    # �ϸ�ũ ���� APP_URLCONF�� �����ϰ� �̸������� 'bookmark'��� ����
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # Class-based views for Bookmark app - �Ʒ��� �ڵ���� APP_URLCONF �� �ű�Ƿ� �ּ�ó��

    # �並 Ŭ������ ��� �����ϱ� ���� �� URL�� ���� �ش� Ŭ���� �� as_view �޼ҵ带 ����
    # URL /bookmark/��û�� ó���� �� Ŭ������ BookmarkLV�� ����, URL ������ �̸��� 'index'�� ���
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/���� ��û�� ó���� �� Ŭ������ BookmarkDV�� ����, URL ������ �̸��� 'detail'�� ���
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
