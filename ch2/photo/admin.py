# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
"""
foreign key로 연결된 Album, Photo 테이블 간에는 1:N 관계가 성립되므로, 앨범 객체를 보여줄 때 객체에 연결된 사진 객체들을 같이 보여줄 수 있습니다.
같이 보여주는 형식은 StackedInline, TabularInline 두 가지가 있는데 여기서는 StackedInline, 즉 세로로 나열되는 형식으로 보여줍니다.
PhotoInline 클래스에서 이런 사항을 정의하고 있습니다. 참고로 TabularInline은 테이블 모양처럼 행으로 나열되는 형식입니다.
"""
class PhotoInline(admin.StackedInline):

    # 추가로 보여주는 테이블은 Photo 테이블입니다.
    model = Photo
    # 이미 입력된 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수는 2개입니다.
    extra = 2

class AlbumAdmin(admin.ModelAdmin):

    # 앨범 객체를 보여줄 때 PhotoInline 클래스에서 정의한 사항을 같이 보여줍니다.
    inlines = [PhotoInline]
    list_display = ('name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)