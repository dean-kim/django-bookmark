# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.utils.encoding import unicode_literals # Python 2.x 지원용

# Create your models here.

# @python_2_unicode_compatible # Python 2.x 지원용

# django.db.models.Model 클래스를 상속받아서 정의
class Bookmark(models.Model):
    # title 컬럼은 공백값(blank)을 가질 수도 있고 값이 없을(null) 수도 있음
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    # 객체를 문자열로 표현할 때 사용하는 함수
    def __str__(self):
        return self.title