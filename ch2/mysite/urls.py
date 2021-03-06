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

# static() 함수를 임포트합니다. static() 함수는 정적 파일을 처리하는 뷰를 호출하도록 그에 맞는 URL 패턴을 반환하는 함수입니다.
from django.conf.urls.static import static

# settings 변수를 임포트합니다. settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체를 가리키는 reference입니다.
from django.conf import settings

from mysite.views import HomeView

# 계정 등록을 처리하는 뷰를 임포트.
# UserCreateView는 계정을 추가하는 뷰, UserCreateDoneTV는 계정 생성이 완료된 후에 보여줄 화면을 처리하는 뷰
from mysite.views import UserCreateView, UserCreateDoneTV

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

    # 장고의 인증 URL(django.contrib.auth.urls)를 가져와서 사용.
    # 장고의 URLconf에는 /login/, /logout/ 처럼 URL이 정의되어 있어서 그 앞에 URL추가를 원한다면 표시해야 함.
    # 로그인에 필요한 URL은 /accounts/login/, 비번 변경은 /accounts/password_change
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # 계정 생성(가입) 처리를 하는 URL
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    # 계정 생성 완료 메세지를 보여주기 위한 URL
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^$', HomeView.as_view(), name='home'),

    # 북마크 앱의 APP_URLCONF를 포함하고 이름공간을 'bookmark'라고 지정
    url(r'^bookmark/', include('bookmark.urlss', namespace='bookmark')),
    url(r'^blog/', include('blog.urlss', namespace='blog')),

    # 포토 앱의 APP_URLCONF를 포함하고, 이름공간을 'photo'라고 지정합니다.
    url(r'^photo/', include('photo.urls', namespace='photo')),

    # Class-based views for Bookmark app - 아래의 코드들은 APP_URLCONF 로 옮기므로 주석처리

    # 뷰를 클래스형 뷰로 정의하기 위해 각 URL에 따른 해당 클래스 및 as_view 메소드를 지정
    # URL /bookmark/요청을 처리할 뷰 클래스를 BookmarkLV로 지정, URL 패턴의 이름은 'index'로 명명
    # url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    # URL /bookmark/숫자 요청을 처리할 뷰 클래스를 BookmarkDV로 지정, URL 패턴의 이름은 'detail'로 명명
    # url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    """
    기존 URL 패턴에 static() 함수가 반환하는 URL 패턴을 추가합니다. static() 함수 형식은 다음과 같습니다.
    static(prefix, view=django.views.static.serve, **kwargs)
    즉 settings.MEDIA_URL로 정의된 /media/ URL 요청이 오면 django.views.static.serve() 뷰 함수가 처리하고,
    이 뷰 함수에 document_root=settings.MEDIA_ROOT 키워드 인자가 전달됩니다.
    """
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
