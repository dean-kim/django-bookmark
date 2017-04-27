# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# �� �ۼ��� �ʿ��� Ŭ������ ������ �並 ����Ʈ
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

# ���̺� ��ȸ�� ���� Post �� Ŭ������ ����Ʈ
from blog.models import Post

# Create your views here.

# ListView
# ListView ���׸� �並 ��ӹ޾� PostLV Ŭ������ �並 ����
# ListView ���׸� ��� ���̺�κ��� ��ü ����Ʈ�� ������ �� ����Ʈ�� �����.
class PostLV(ListView):
    # PostLV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ���ø� ������ 'blog/post_all.html'�� ������.
    # ���ø� ������ �������� ������ ����Ʈ ���ø� ���� 'blog/post_list.html�� ��.'
    template_name = 'blog/post_all.html'
    # ���ø� ���Ϸ� �Ѱ��ִ� ��ü ����Ʈ�� ���� ���ؽ�Ʈ �������� 'posts'�� ����.
    # ������ ���ؽ�Ʈ �������� �����ص� ����Ʈ ���ؽ�Ʈ �������� 'object_list' ���� ��� ������.
    context_object_name = 'posts'
    # �� �������� �����ִ� ��ü ����Ʈ�� ���ڴ� 2, paginate_by �Ӽ��� �����ϸ� ��� �����ϴ� ����¡ ����� ����� �� ����.
    # ����¡ ����� Ȱ��ȭ�Ǹ� ��ü ����Ʈ �ϴܿ� �������� �̵��� �� �ִ� ��ư�� ���� �� ����.
    paginate_by = 2

# DetailView
# DetailView ���׸� �並 ��ӹ޾� PostDV Ŭ������ �並 ����
# DetailView ���׸� ��� ���̺�κ��� Ư�� ��ü�� ������ �� ��ü�� �� ������ �����.
# ���̺��� Ư�� ��ü�� ��ȸ�ϱ� ���� Ű�� �⺻ Ű ��� slug �Ӽ��� ����ϰ� ����. �� slug �Ķ���ʹ� URLconf���� ������ ��� �Ѱ���.
class PostDV(DetailView):
    # PostDV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post

# ArchiveView
# ArchiveIndexView ���׸� �並 ��ӹ޾� PostAV Ŭ������ �並 ����
# ArchiveIndexView ���׸� ��� ���̺�κ��� ��ü ����Ʈ�� ������ ��¥ �ʵ带 �������� �ֽ� ��ü�� ���� �����.
class PostAV(ArchiveIndexView):
    # PostAV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ������ �Ǵ� ��¥ �ʵ�� 'modify_date'�÷��� ���, ���� ��¥�� �ֱ��� ����Ʈ�� ���� �����.
    date_field = 'modify_date'

# YearArchiveView ���׸� �並 ��ӹ޾� PostYAV Ŭ������ �並 ����
# YearArchiveView ���׸� ��� ���̺�κ��� ��¥ �ʵ��� ������ �������� ��ü ����Ʈ�� ������ �� ��ü���� ���� ���� ����Ʈ�� ���.
# ��¥ �ʵ��� ���� �Ķ���ʹ� URLconf���� ������ ��� �Ѱ���.
class PostYAV(YearArchiveView):
    # PostYAV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ������ �Ǵ� ��¥ �ʵ�� 'modify_date'�÷��� ���, ���� ��¥�� 'YYYY��'�� ����Ʈ�� �˻��� �� ����Ʈ���� ���� ���� �����.
    date_field = 'modify_date'
    # make_object_list �Ӽ��� True �̸� �ش� ������ �ش��ϴ� ��ü�� ����Ʈ�� ���� ���ø��� �Ѱ���
    # ���ø� ���Ͽ��� object_list�� ����� �� ����. ����Ʈ�� 'False'��
    make_object_list = True

# MonthArchiveView ���׸� �並 ��ӹ޾� PostMAV Ŭ������ �並 ����
# MonthArchiveView ���׸� ��� ���̺�κ��� ��¥ �ʵ��� ������ �������� ��ü ����Ʈ�� ������ �� ����Ʈ�� ���.
# ��¥ �ʵ��� ����, �� �Ķ���ʹ� URLconf���� ������ ��� �Ѱ���.
class PostMAV(MonthArchiveView):
    # PostMAV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ������ �Ǵ� ��¥ �ʵ�� 'modify_date'�÷��� ���. ���� ��¥�� ������ �������� ����Ʈ�� �˻��� �� ����Ʈ���� ����Ʈ�� �����.
    date_field = 'modify_date'

# DayArchiveView ���׸� �並 ��ӹ޾� PostDAV Ŭ������ �並 ����
# DayArchiveView ���׸� ��� ���̺�κ��� ��¥ �ʵ��� �������� �������� ��ü ����Ʈ�� ������ �� ����Ʈ�� ���.
# ��¥ �ʵ��� ��,��,�� �Ķ���ʹ� URLconf���� ������ ��� �Ѱ���.
class PostDAV(DayArchiveView):
    # PostDAV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ������ �Ǵ� ��¥ �ʵ�� 'modify_date'�÷��� ���. ���� ��¥�� �������� �������� ����Ʈ�� �˻��� �� ����Ʈ���� ����Ʈ�� �����.
    date_field = 'modify_date'

# TodayArchiveView ���׸� �並 ��ӹ޾� PostTAV Ŭ������ �並 ����
# TodayArchiveView ���׸� ��� ���̺�κ��� ��¥ �ʵ��� ������ ��ü ����Ʈ�� ������ �� ����Ʈ�� �����.
# ���� ��¥�� ���� �����Ϸ� �����Ѵٴ� �� �̿ܿ��� DayArchiveView�� ����
class PostTAV(TodayArchiveView):
    # PostTAV Ŭ������ ��� ���̺��� Post ���̺�.
    model = Post
    # ������ �Ǵ� ��¥ �ʵ�� 'modify_date'�÷��� ���. ���� ��¥�� ������ ����Ʈ�� �˻��� �� ����Ʈ���� ����Ʈ�� �����.
    date_field = 'modify_date'