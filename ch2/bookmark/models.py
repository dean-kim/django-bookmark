# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.utils.encoding import unicode_literals # Python 2.x 지원용

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# @python_2_unicode_compatible # Python 2.x 지원용

# django.db.models.Model 클래스를 상속받아서 정의
class Bookmark(models.Model):
    # title 컬럼은 공백값(blank)을 가질 수도 있고 값이 없을(null) 수도 있음
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    """
    로그인한 사용자는 여러 개의 북마크를 생성할 수 있으므로 Bookmark와 User 테이블 사이는 N:1관계, 장고에서 N:1 관계는 외래 키로 표현합니다.
    owener 필드는 NULL 값을 가질 수 있어야 함(null=True). 이미 Bookmark 테이블에 레코드가 존재한 상태에서 지금 owner 필드를 추가하면
    기존 레코드의 owner 필드에는 NULL 값으로 채워야 하기 때문임. 디폴트 값을 지정해도 되지만 이 예제에서는 Null 값을 사용함.
    """
    owner = models.ForeignKey(User, null=True)

    # 객체를 문자열로 표현할 때 사용하는 함수
    def __str__(self):
        return self.title