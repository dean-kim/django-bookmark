# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

# Register your models here.

# PostAdmin Ŭ������ Post Ŭ������ Admin ���������� � ������� ���̴��� �����ϴ� Ŭ����.
class PostAdmin(admin.ModelAdmin):
    # Post ��ü�� ������ �� title�� modify_date�� ȭ�鿡 ����ϵ��� ����
    list_display = ('title', 'modify_date')
    # modify_date �÷��� ����ϴ� ���� ���̵�ٸ� �����ֵ��� ����.
    list_filter = ('modify_date',)
    # �˻��ڽ��� ǥ���ϰ�, �Էµ� �ܾ�� title�� content �÷����� �˻��ϵ��� ��.
    search_fields = ('title', 'content')
    # slug �ʵ�� title �ʵ带 ����� �̸� ä�������� ��.
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register() �Լ��� ����� Post�� PostAdmin Ŭ������ Admin �������� �����.
admin.site.register(Post, PostAdmin)