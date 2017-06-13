# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 뷰 작성에 필요한 클래스형 제레릭 뷰를 임포트
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

# 테이블 조회를 위해 Post 모델 클래스를 임포트
from blog.models import Post

# REST
from django.http.response import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, mixins

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin


# Create your views here.

# ListView
# ListView 제네릭 뷰를 상속받아 PostLV 클래스형 뷰를 정의
# ListView 제네릭 뷰는 테이블로부터 객체 리스트를 가져와 그 리스트를 출력함.
class PostLV(ListView):
    # PostLV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 템플릿 파일을 'blog/post_all.html'로 지정함.
    # 템플릿 파일을 지정하지 않으면 디폴트 템플릿 명인 'blog/post_list.html이 됨.'
    template_name = 'blog/post_all.html'
    # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 'posts'로 지정.
    # 별도록 컨텍스트 변수명을 지정해도 디폴트 컨텍스트 변수명인 'object_list' 역시 사용 가능함.
    context_object_name = 'posts'
    # 한 페이지에 보여주는 객체 리스트의 숫자는 2, paginate_by 속성을 정의하면 장고가 제공하는 페이징 기능을 사용할 수 있음.
    # 페이징 기능이 활성화되면 객체 리스트 하단에 페이지를 이동할 수 있는 버튼을 만들 수 있음.
    paginate_by = 2

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# DetailView
# DetailView 제네릭 뷰를 상속받아 PostDV 클래스형 뷰를 정의
# DetailView 제네릭 뷰는 테이블로부터 특정 객체를 가져와 그 객체의 상세 정보를 출력함.
# 테이블에서 특정 객체를 조회하기 위한 키는 기본 키 대신 slug 속성을 사용하고 있음. 이 slug 파라미터는 URLconf에서 추출해 뷰로 넘겨줌.
class PostDV(DetailView):
    # PostDV 클래스의 대상 테이블은 Post 테이블.
    model = Post

# ArchiveView
# ArchiveIndexView 제네릭 뷰를 상속받아 PostAV 클래스형 뷰를 정의
# ArchiveIndexView 제네릭 뷰는 테이블로부터 객체 리스트를 가져와 날짜 필드를 기준으로 최신 객체를 먼저 출력함.
class PostAV(ArchiveIndexView):
    # PostAV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date'컬럼을 사용, 변경 날짜가 최근인 포스트를 먼저 출력함.
    date_field = 'modify_date'

# YearArchiveView 제네릭 뷰를 상속받아 PostYAV 클래스형 뷰를 정의
# YearArchiveView 제네릭 뷰는 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와 그 객체들이 속한 월을 리스트로 출력.
# 날짜 필드의 연도 파라미터는 URLconf에서 추출해 뷰로 넘겨줌.
class PostYAV(YearArchiveView):
    # PostYAV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date'컬럼을 사용, 변경 날짜가 'YYYY년'인 포스트를 검색해 그 포스트들의 변경 월을 출력함.
    date_field = 'modify_date'
    # make_object_list 속성이 True 이면 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨줌
    # 템플릿 파일에서 object_list를 사용할 수 있음. 디폴트는 'False'임
    make_object_list = True

# MonthArchiveView 제네릭 뷰를 상속받아 PostMAV 클래스형 뷰를 정의
# MonthArchiveView 제네릭 뷰는 테이블로부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와 그 리스트를 출력.
# 날짜 필드의 연도, 월 파라미터는 URLconf에서 추출해 뷰로 넘겨줌.
class PostMAV(MonthArchiveView):
    # PostMAV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date'컬럼을 사용. 변경 날짜의 연월을 기준으로 포스트를 검색해 그 포스트들의 리스트를 출력함.
    date_field = 'modify_date'

# DayArchiveView 제네릭 뷰를 상속받아 PostDAV 클래스형 뷰를 정의
# DayArchiveView 제네릭 뷰는 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와 그 리스트를 출력.
# 날짜 필드의 연,월,일 파라미터는 URLconf에서 추출해 뷰로 넘겨줌.
class PostDAV(DayArchiveView):
    # PostDAV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date'컬럼을 사용. 변경 날짜의 연월일을 기준으로 포스트를 검색해 그 포스트들의 리스트를 출력함.
    date_field = 'modify_date'

# TodayArchiveView 제네릭 뷰를 상속받아 PostTAV 클래스형 뷰를 정의
# TodayArchiveView 제네릭 뷰는 테이블로부터 날짜 필드의 오늘인 객체 리스트를 가져와 그 리스트를 출력함.
# 오늘 날짜를 기준 연월일로 지정한다는 점 이외에는 DayArchiveView와 동일
class PostTAV(TodayArchiveView):
    # PostTAV 클래스의 대상 테이블은 Post 테이블.
    model = Post
    # 기준이 되는 날짜 필드는 'modify_date'컬럼을 사용. 변경 날짜가 오늘인 포스트를 검색해 그 포스트들의 리스트를 출력함.
    date_field = 'modify_date'

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.object.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

# TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = ['slug': 'auto-filling-do-not-input']
    #fields = ['title', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_chage_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')