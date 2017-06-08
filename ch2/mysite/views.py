# -*- coding: euckr -*-
# coding=utf-8

from django.views.generic.base import TemplateView

# 제네릭 뷰 CreateView를 임포트, 이 뷰는 테이블의 레코드를 생성하기 위해 이에 필요한 폼을 보여주고, 폼의 입력을 받아서 테이블의 레코드를 생성하는 뷰.
# 제네릭 뷰 중에서 이렇게 테이블의 변경 처리에 관련된 뷰를 편집용 제네릭 뷰라고 하는데 CreateView 외에도 UpdateView, DeleteView, FormView가 있음.
from django.views.generic.edit import CreateView

# UserCreationForm를 임포트, UserCreationForm은 User 모델의 객체를 생성하기 위해 보여주는 폼. 장고 기본 제공 뷰임.
from django.contrib.auth.forms import UserCreationForm

# reverse_lazy() 및 reverse() 함수는 인자로 URL 패턴명을 받음. URL 패턴명을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어야 함.
# 지금 작성하고 있는 views.py 모듈이 로딩되고 처리되는 시점에 urls.py 모듈이 로딩되지 않을 수도 있으므로, reverse() 함수 대신 reverse_lazy() 함수를 임포트
from django.core.urlresolvers import reverse_lazy


#--- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'


#--- User Creation
# CreateView를 상속받아 UserCreateView 클래스형 뷰를 작성. UserCreateView뷰는 '/accounts/register/' URL을 처리하는 뷰
# 이 예제처럼 중요한 몇 가지 클래스 속성만 정의해주면 적절한 폼을 보여주고, 폼에 입력된 내용에서 에러 여부를 체크한 후 에러가 없으면 입력된 내용으로 테이블에 레코드를 생성함.
class UserCreateView(CreateView):

    # 화면에 보여줄 템플릿 이름을 지정, 템플릿의 내용은 다음 줄의 form_class 속성에 지정된 폼을 사용함.
    template_name = 'registration/register.html'

    # 템플릿에서 사용할 폼은 장고의 기본 폼인 UserCreationForm을 사용
    form_class = UserCreationForm

    # 폼에 입력된 내용에 에러가 없고 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정. 여기서는 'accounts/register/done'으로 이동
    success_url = reverse_lazy('register_done')

# 'accounts/register/done' 을 처리해주는 뷰, 특별한 로직 없이 템플릿만 보여주면 되므로 TemplateView 제네릭 뷰를 상속받아 작성함.
class UserCreateDoneTV(TemplateView):

    # User 레코드 생성, 즉 가입 처리가 완료된 후에 사용자에게 보여줄 템플릿의 파일명을 지정함.
    template_name = 'registration/register_done.html'