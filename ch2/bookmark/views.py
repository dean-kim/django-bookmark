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

# 편집용 제네릭 뷰인 CreateView, UpdateView, DeleteView를 임포트
# CreateView: 테이블 레코드 생성, UpdateView: 테이블 레코드 수정, DeleteView: 테이블 레코드 삭제
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# reverse_lazy(), reverse() 함수는 URL 패턴명을 인자로 받음.
# URL 패턴명을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어야 함.
# 지금 작성하고 있는 views.py 모듈이 로딩되고 처리되는 시점에 urls.py 모듈이 로딩되지 않을 수 있으므로, reverse() 대신 reverse_lazy()를 임포트
from django.core.urlresolvers import reverse_lazy

# LoginRequiredMixin 클래스 임포트, @login_required() 데코레이터 기능을 클래스에 적용할 때 사용.
from mysite.views import LoginRequiredMixin

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

# LoginRequiredMixin, CreateView를 상속받아 BookmarkCreateView 뷰를 작성
# LoginRequiredMixin 클래스를 상속받는 클래스는 로그인된 경우만 접근이 가능함. 만일 로그인이 되지 않은 상태에서
# BookmarkCreateView 뷰를 호출하면 로그인 페이지로 이동
# CreateView 클래스를 상속받는 클래스는 예제처럼 중요한 몇 가지 클래스 속성만 정의하면 적절한 폼을 보여주고,
# 폼에 입력된 내용에서 에러 여부를 체크한 후 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성함.
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    # CreateView 기능을 적용할 대상 테이블을 Bookmark 테이블로 지정.
    model = Bookmark
    # CreateView 기능에 따라 폼을 보여줄 때, Bookmark 테이블의 title과 url 필드에 대한 입력 폼을 보여줌.
    fields = ['title', 'url']
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정.
    success_url = reverse_lazy('bookmark:index')

    # 폼에 입력된 내용에 대해 유효성 검사를 수행해 에러가 없는 경우, form_valid() 메소드를 호출.
    def form_valid(self, form):
        # 폼의 owner 필드에는 현재 로그인된 사용자의 User 객체를 할당.
        form.instance.owner = self.request.user
        # 부모 클래스, 즉 CreateView 클래스의 form_valid() 메소드를 호출.
        return super(BookmarkCreateView, self).form_valid(form)

# LoginRequiredMixin, ListView 상속받아 BookmarkChangeLV 뷰를 작성.
# BookmarkChangeLV 뷰의 기능은 Bookmark 테이블에서 현재 로그인된 사용자에게 콘텐츠 변경이 허용된 레코드 리스트를 화면에 출력.
# 이 클래스도 LoginRequiredMixin 클래스를 상속받고 있어서 login_required() 데코레이터 기능을 제공함.
# ListView 제네릭 뷰를 상속받고 있으므로 객체의 리스트만 지정해주면 그 리스트를 화면에 출력함.
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    # 리스트를 화면에 출력 시 사용할 템플릿의 이름을 지정
    template_name = 'bookmark/bookmark_change_list.html'

    # get_queryset() 메소드는 화면에 출력할 레코드 리스트를 반환.
    # Bookmark 테이블의 레코드 중에서 owner 필드가 로그인한 사용자인 레코드만 필터링해 그 리스트를 반환.
    # 이 줄에 의해 콘텐츠는 콘텐츠를 생성한 소유자만 변경할 수 있음.
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

# LoginRequiredMixin, UpdateView를 상속받아 BookmarkUpdateView를 작성.
# 이 클래스도 LoginRequiredMixin 클래스를 상속받고 있어서 login_required() 데코레이터 기능을 제공함.
# UpdateView 클래스를 상속받는 클래스는 예제처럼 중요한 몇 가지 클래스 속성만 정의해주면 기존 레코드 중에서 지정된 레코드 하나에 대한 내용을 폼으로 보여주고,
# 폼에서 수정 입력된 내용에서 에러 여부를 체크하고, 에러가 없으면 입력된 내용으로 테이블의 레코드를 수정함.
class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    # UpdateView 기능을 적용할 대상 테이블을 Bookmark 테이블로 지정.
    model = Bookmark
    # UpdateView 기능에 따라 폼을 보여줄 때, Bookmark 테이블의 특정 레코드를 선택하고, 그 레코드의 title, url 필드로 폼을 구성해 화면에 보여줌.
    fields = ['title', 'url']
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정.
    success_url = reverse_lazy('bookmark:index')

# LoginRequiredMixin, DeleteView 상속받아 BookmarkDeleteView를 작성.
# 이 클래스도 LoginRequiredMixin 클래스를 상속받고 있어서 login_required() 데코레이터 기능을 제공함.
# DeleteView 클래스를 상속받는 클래스는 예제처럼 중요한 몇 가지 클래스만 속성만 정의해주면 기존 레코드 중에서 지정된 레코드를 삭제할 것인지 확인하는 페이지 보여줌.
# 사용자가 확인 응답을 하면 해당 레코드를 삭제.
class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    # DeleteView 기능을 적용할 대상 테이블을 Bookmark 테이블로 지정.
    model = Bookmark
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정.
    success_url = reverse_lazy('bookmark:index')