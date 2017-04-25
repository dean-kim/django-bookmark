# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

"""
클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView를 import
generic view?
: 장고에서 기본적으로 제공하는 클래스, 웹 프로그램 개발 시 공통적으로 사용하는 로직을 미리 반영한 클래스임.
  generic view를 상속받아서 필요한 속성과 메소드를 오버라이딩하여 사용할 수 있다.
"""
from django.views.generic import ListView, DetailView
# 테이블 조회를 위해 모델 클래스를 import
from bookmark.models import Bookmark

# Create your views here.

# ListView
"""
BookmarkLV는 테이블의 레코드 리스트를 보여주기 위한 뷰, ListView를 상속 받음.
그리고 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2개 있음.
1. 컨텍스트 변수로 object_list를 사용
2. 템플릿 파일을 '모델명소문자_list.html' 형식의 이름으로 지정
   (이 경우라면 bookmark_list.html)
"""
class BookmarkLV(ListView):
    model = Bookmark

# DetailView
"""
BookmarkDV는 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰, DetailView를 상속 받음.
그리고 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2개 있음
1. 컨텍스트 변수로 object를 사용
2. 템플릿 파일을 '모델명소문자_detail.html' 형식의 이름으로 지정
   (이 경우라면 bookmark_detail.html)
DetailView를 상속받는 경우 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 됨.
만일 테이블에서 기본 키로 조회해서 특정 객체를 가져오는 경우에는 테이블명 즉 모델 클래스명만 지정해주면 됨.
조회 시 사용할 기본 키 값은 URLconf에서 추출해 뷰로 넘어온 파라미터를 사용함.
"""
class BookmarkDV(DetailView):
    model = Bookmark