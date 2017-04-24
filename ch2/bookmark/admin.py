# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

# BookmarkAdmin 클래스는 Bookmark 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    # Bookmark 내용을 보여줄 때 title과 url을 화면에 출력
    list_display = ('title', 'url')

# admin.site.register() 함수를 사용해서 Bookmark와 BookmarkAdmin 클래스를 등록
admin.site.register(Bookmark, BookmarkAdmin)