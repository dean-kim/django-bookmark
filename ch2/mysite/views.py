# -*- coding: euckr -*-
# coding=utf-8

from django.views.generic.base import TemplateView

# ���׸� �� CreateView�� ����Ʈ, �� ��� ���̺��� ���ڵ带 �����ϱ� ���� �̿� �ʿ��� ���� �����ְ�, ���� �Է��� �޾Ƽ� ���̺��� ���ڵ带 �����ϴ� ��.
# ���׸� �� �߿��� �̷��� ���̺��� ���� ó���� ���õ� �並 ������ ���׸� ���� �ϴµ� CreateView �ܿ��� UpdateView, DeleteView, FormView�� ����.
from django.views.generic.edit import CreateView

# UserCreationForm�� ����Ʈ, UserCreationForm�� User ���� ��ü�� �����ϱ� ���� �����ִ� ��. ��� �⺻ ���� ����.
from django.contrib.auth.forms import UserCreationForm

# reverse_lazy() �� reverse() �Լ��� ���ڷ� URL ���ϸ��� ����. URL ���ϸ��� �ν��ϱ� ���ؼ��� urls.py ����� �޸𸮿� �ε��Ǿ�� ��.
# ���� �ۼ��ϰ� �ִ� views.py ����� �ε��ǰ� ó���Ǵ� ������ urls.py ����� �ε����� ���� ���� �����Ƿ�, reverse() �Լ� ��� reverse_lazy() �Լ��� ����Ʈ
from django.core.urlresolvers import reverse_lazy


#--- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'


#--- User Creation
# CreateView�� ��ӹ޾� UserCreateView Ŭ������ �並 �ۼ�. UserCreateView��� '/accounts/register/' URL�� ó���ϴ� ��
# �� ����ó�� �߿��� �� ���� Ŭ���� �Ӽ��� �������ָ� ������ ���� �����ְ�, ���� �Էµ� ���뿡�� ���� ���θ� üũ�� �� ������ ������ �Էµ� �������� ���̺� ���ڵ带 ������.
class UserCreateView(CreateView):

    # ȭ�鿡 ������ ���ø� �̸��� ����, ���ø��� ������ ���� ���� form_class �Ӽ��� ������ ���� �����.
    template_name = 'registration/register.html'

    # ���ø����� ����� ���� ����� �⺻ ���� UserCreationForm�� ���
    form_class = UserCreationForm

    # ���� �Էµ� ���뿡 ������ ���� ���̺� ���ڵ� ������ �Ϸ�� �Ŀ� �̵��� URL�� ����. ���⼭�� 'accounts/register/done'���� �̵�
    success_url = reverse_lazy('register_done')

# 'accounts/register/done' �� ó�����ִ� ��, Ư���� ���� ���� ���ø��� �����ָ� �ǹǷ� TemplateView ���׸� �並 ��ӹ޾� �ۼ���.
class UserCreateDoneTV(TemplateView):

    # User ���ڵ� ����, �� ���� ó���� �Ϸ�� �Ŀ� ����ڿ��� ������ ���ø��� ���ϸ��� ������.
    template_name = 'registration/register_done.html'