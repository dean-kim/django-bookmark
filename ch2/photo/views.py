# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 리다이렉트를 위한 단축 함수 redirect 임포트
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

# forms.py에서 정의한 PhotoInlineFormSet 폼셋을 임포트
# 폼셋이란 동일한 폼 여러 개로 구성됨 폼. 인라인 폼셋이란 메인 폼에 딸려 있는 폼셋을 말함, 테이블 간의 관계가
# 1:N인 경우, N테이블의 레코드 여러 개를 한꺼번에 입력받기 위한 폼으로 사용
from photo.forms import PhotoInlineFormSet

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo

#--- Add/Change/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

    def form_vaild(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

class PhotoDeleteView(LoginRequiredMixin, DetailView):
    model = Photo
    success_url = reverse_lazy('photo:index')

#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

class AlbumDeleteView(LoginRequiredMixin, ListView):
    model = Album
    success_url = reverse_lazy('photo:index')

#--- InlineFormSet View
#--- Add/Update for Album
# LoginRequiredMixin 및 CreateView를 상속받아 AlbumPhotoCV 뷰를 작성
# LoginRequiredMixin 클래스는 @login_required 데코레이터 기능을 함. 그리고 CreateView 클래스를 상속받는 클래스는 여기처럼 중요한
# 몇 가지 클래스 속성만 정의해주면, 적절한 폼을 보여주고 폼에 입력된 내용에서 에러 여부를 체크하고 에러가 없으면 입력된 내용을 테이블에 레코드를 생성
class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    # CreateView 기능을 적용할 대상 테이블을 Album 테이블로 지정
    model = Album
    # CreateView 기능에 따라 폼을 보여줄 때, Album 테이블의 name, description 필드에 대한 입력 폼을 보여줌.
    fields = ['name', 'description']
    # 템플릿 이름은 'photo/album_form.html' 파일. 디폴트 파일명과 동일하므로 생략 가능.
    template_name = 'photo/album_form.html'

# 장고에서 제공하는 디폴트 컨텍스트 변수 이외에 추가적인 컨텍스트 변수를 정의하기 위해 get_context_data() 메소드를 오버라이딩 정의함.
    def get_context_data(self, **kwargs):
        # AlbumPhotoCV 부모 클래스의 get_context_data() 호출해 기본 컨텍스트 변수를 설정.
        # 이 예제에서는 기본 컨텍스트 변수 이외에도 메인 폼도 컨텍스트 변수에 추가함.
        context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
        # POST 요청인 경우, formset 컨텍스트 변수를 request.POST와 request.FILES 파라미터를 사용해 지정.
        # request.FILES 파라미터를 추가한 이유는 파일 업로드가 이뤄지기 때문임.
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            # GET 요청인 경우, formset 컨텍스트 변수에 빈 폼셋을 지정함.
            context['formset'] = PhotoInlineFormSet()
        # context라는 컨텍스트 변수 사전을 반환.
        return context

# 폼에 입력된 내용에 대해 유효성 검사를 수행해 에러가 없는 경우, form_valid() 메소드를 호출
    def form_valid(self, form):
        # 폼의 owner 필드에는 현재 로그인된 사용자의 User 객체를 할당. 즉, 앨범 폼의 owner 필드를 자동으로 지정
        form.instance.owner = self.request.user
        # 앞에서 정의한 get_context_data() 메소드를 호출해, context 컨텍스트 사전을 지정
        context = self.get_context_data()
        formset = context['formset']
        # 폼셋에 들어 있는 각 폼의 owner 필드에 현재 로그인된 사용자의 User 객체를 할당. 즉 폼셋에 들어 있는 각 사진 폼의 owner 필드를 자동으로 지정
        for photoform in formset:
            photoform_instance.owner = self.request.user
        # 폼셋에 들어 있는 각 사진 폼의 데이터가 모두 유효한지 확인
        if formset.is_valid():
            # form.save()를 호출해 폼의 데이터를 테이블에 저장. 즉, 앨범 레코드를 하나 생성한 것임.
            self.object = form.save()
            # 폼셋의 메인 객체를 방금 테이블에 저장한 객체로 지정함.
            formset.instance = self.object
            # formset.save()를 호출해 폼셋의 데이터를 테이블에 저장
            # 앞서 생성한 앨범 레코드에 1:N 관계로 연결된 여러 개의 사진 레코드를 테이블에 저장
            formset.save()
            # 마지막으로 앨범 객체의 get_absolute_url() 메소드를 호출해 페이지를 이동시킴. 즉, 앨범 상세 페이지로 리다이렉트됨.
            return redirect(self.object.get_absolute_url())
        else:
            # 폼셋의 데이터가 유효하지 않으면, 다시 메인 폼 및 인라인 폼셋을 출력.
            # 이때의 폼과 폼셋에는 직전에 사용자가 입력한 데이터를 다시 보여줌.
            return self.render_to_response(self.get_context_data(form=form))

# LoginRequiredMixin, UpdateView 상속받아 AlbumPhotoUV 뷰를 작성
# LoginRequiredMixin 클래스는 @login_required 데코레이터 기능을 함.
# 그리고 UpdateView 클래스를 상속받는 클래스는 예제처럼 중요한 몇 가지 클래스 속성만 정의해주면, 기존 레코드 중에서 지정된 레코드 하나에 대한
# 내용을 폼으로 보여주고, 폼에서 수정 입력된 내용에서 에러 여부를 체크하고, 에러가 없으면 입력된 내용으로 테이블의 레코드를 수정함.
class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
    # UpdateView 기능을 적용할 대상 테이블을 Album 테이블로 지정.
    model = Album
    # UpdateView 기능에 따라 폼을 보여줄 때, Album 테이블의 특정 레코드를 선택하고, 그 레코드의 name, description 필드로 폼을 구성해 화면에 보여줌.
    fields = ['name', 'description']
    # 템플릿 이름은 'photo/album_form.html' 파일. 디폴트 파일명과 동일하므로 생략 가능.
    template_name = 'photo/album_form.html'

    # 장고에서 제공하는 디폴트 컨텍스트 변수 이외에 추가적인 컨텍스트 변수를 정의하기 위해 get_context_data() 메소드를 오버라이딩 정의함.
    def get_context_data(self, **kwargs):
        # AlbumPhotoUV 부모 클래스의 get_context_data() 호출, 기본 컨텍스트 변수를 설정.
        # 이 예제에서는 기본 컨텍스트 변수 이외에 메인 폼도 컨텍스트 변수에 추가함.
        context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
        # POST 요청인 경우, formset 컨텍스트 변수를 request.POST와 request.FILES 파라미터를 사용해 지정.
        # 또한 instance 파라미터에 현재의 앨범 객체를 지정
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            # GET 요청인 경우, formset 컨텍스트 변수에 현재의 앨범 객체와 연결된 폼셋을 지정
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        # context라는 컨텍스트 변수 사전을 반환
        return context

    # 폼에 입력된 내용에 대해 유효성 검사를 수행해 에러가 없는 경우, form_valid() 메소드를 호춞.
    def form_valid(self, form):
        # 앞서 정의한 get_context_data() 메소드를 호출해 context 컨텍스트 사전을 지정.
        context = self.get_context_data()
        formset = context['formset']
        # 폼셋에 들어 있는 각 사진 폼의 데이터가 모두 유효한지 확인
        if formset.is_valid():
            # form.save()를 호출해 폼의 데이터를 테이블에 저장. 즉, 현재의 앨범 레코드를 수정한 것임.
            self.object = form.save()
            # 폼셋의 메인 객체를 방금 테이블에 저장한 객체로 지정.
            formset.instance = self.object
            # formset.save()를 호출해 폼의 데이터를 테이블에 저장. 앞서 수정한 앨범 레코드에 1:N 관계로 연결된 여러 개의 사진 레코드를 테이블에 저장함.
            formset.save()
            # 앨범 객체의 get_absolute_url() 메소드를 호출해 페이지를 이동시킴. 즉, 앨범 상세 페이지로 리다이렉트됨.
            return redirect(self.object.get_absolute_url())
        else:
            # 폼셋의 데이터가 유효하지 않으면, 다시 메인 폼 및 인라인 폼셋을 출력함.
            # 이때의 폼과 폼셋에는 직전에 사용자가 입력한 데이터를 다시 보여줌.
            return self.render_to_response(self.get_context_data(form=form))