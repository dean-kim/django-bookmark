# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

# ThumbnailImageField를 임포트합니다. ThumbnailImageField 필드 클래스는 사진에 대한 원본 이미지와 썸네일 이미지를 모두 저장할 수 있는 빌드로
# 직접 만든 커스텀 필드입니다. 이 커스텀 필드는 fields.py에 정의되어 있습니다.
from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    # Album과 User 테이블 간 관계 및 Photo, User 테이블 간 관계는 모두 N:1 관계이므로, 외래키 관계로 표현
    # 또한 owner 필드는 NULL 값을 가질 수 있도록 정의
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    # get_absolute_url 메소드는 이 메소드가 정의된 객체를 지칭하는 URL을 반환합니다. 메소드 내에서는 장고의 내장 함수인 reverse()를 호출합니다. 여기서는 /photo/album/99/ 형식의 URL을 반환합니다.
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id),)

@python_2_unicode_compatible
class Photo(models.Model):

    # album 컬럼은 Album 테이블에 연결된 외래 키입니다. 즉, 본 사진이 소속된 앨범 객체를 가리키는 reference 역할을 합니다.
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=50)

    """
    image 컬럼은 필드 타입이 ThumbnailImageField입니다. ThumbnailImageField 필드는 사진에 대한 원본 이미지 및 썸네일 이미지 둘 다를 저장할 수 있는
    필드인데, upload_to 옵션으로 저장할 위치를 지정합니다. 'photo/%Y/%m'의 의미는 MEDIA_ROOT로 정의된 디렉토리 하위에 ~/photo/2015/08 처럼
    연도와 월을 포함해 디렉토리를 만들고 그 곳에 업로드하는 사진의 원본 및 썸네일 사진을 저장합니다. 예를 들어 2015년 8월에 사진을 업로드 한다면 다음의
    디렉토리에 사진이 저장될 것 입니다.
    ~/ch2/media/2015/08/
    업로드하는 시점에 디렉토리가 없다면 자동으로 생성됩니다.
    """
    image = ThumbnailImageField(upload_to='photo/%Y/%m')

    # description 컬럼은 TextField를 사용해 여러 줄의 입력이 가능합니다. 컬럼에 대한 레이블은 'Photo Description'이고 내용이 없어도 됩니다. (blank=True)
    description = models.TextField('Photo Description', blank=True)

    # upload_date 컬럼은 날짜와 시간을 입력하는 DateTimeField이며 auto_now_add 속성은 객체가 생성될 때의 시각을 자동으로 기록하게 합니다. 사진이 업로드되는 시간을 자동으로 기록합니다.
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    # Album과 User 테이블 간 관계 및 Photo, User 테이블 간 관계는 모두 N:1 관계이므로, 외래키 관계로 표현
    # 또한 owner 필드는 NULL 값을 가질 수 있도록 정의
    owner = models.ForeignKey(User, null=True)

    # Meta 내부 클래스로, 객체 리스트를 출력할 때의 정렬 기준을 정의힙니다. title 컬럼을 기준으로 오름차순으로 정렬합니다.
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    # get_absolute_url 메소드는 이 메소드가 정의된 객체를 지칭하는 URL을 반환합니다. 메소드 내에서는 장고의 내장 함수인 reverse()를 호출합니다. 여기서는 /photo/album/99/ 형식의 URL을 반환합니다.
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id),)