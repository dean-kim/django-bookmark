# -*- coding: euckr -*-
# -*- coding: utf-8 -*-
# 파이썬 버전 2와 버전 3 간에는 문자열을 처리하는 방식이 다름. 장고에서는 버전 3 방식의 문자열 처리를 기준으로 정하고, 버전 2와의 호환성을 유지하기 위해서 아래 2개의 명령문이 필요
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# reverse() 함수를 사용하기 위해 임포트 reverse() 함수는 URL 패턴을 만들어주는 장고의 내장 함수임.
from django.core.urlresolvers import reverse

from tagging.fields import TagField
# Create your models here.

@python_2_unicode_compatible

class Post(models.Model):
    # title 컬럼은 CharField 이므로 한 줄로 입력.
    # 컬럼에 대한 레이블은 'TITLE'이고 최대 길이는 50글자로 설정
    # 레이블은 폼 화면에 나타나는 문구로 Admin 페이지에서 확인 가능함.
    title = models.CharField('Title', max_length=50)
    # slug 컬럼은 제목의 별칭.
    # SlugField에 unique 옵션을 추가해 특정 포스트를 검색 시 기본 키 대신에 사용됨.
    # allow_unicode 옵션을 추가하면 한글 처리가 가능함.
    # help_text는 해당 컬럼을 설명해주는 문구로 폼 화면에 나타남. Admin 페이지에서 확인 가능.


    """
    - 슬러그란?
    슬러그는 페이지나 포스트를 설명하는 핵심 단어의 집합. 원래 신문이나 잡지 등에서 제목을 쓸 때, 중요한 의미를 포함하는 단어만을 이용해 제목을
    작성하는 방법. 웹 개발 분야에서는 콘텐츠의 고유 주소로 사용되어 콘텐츠의 주소가 어떤 내용인지를 쉽게 이해할 수 있도록 함.
    보통 슬러그는 페이지나 포스트의 제목에서 조사, 전치사, 쉼표, 마침표 등을 빼고 띄어쓰기는 하이픈(-)으로 대체해서 만들며, URL에 사용됨.
    슬러그를 URL에 사용함으로써 검색 엔진에서 더 빨리 페이지를 찾아주고 검색 엔진의 정확도를 높여줌.
    - SlugField 필드 타입
    슬러그는 보통 제목의 단어들을 하이픈으로 연결해 생성하며, URL에서 pk 대신으로 사용되는 경우가 많음. pk를 사용하면 숫자로만 되어 있어 
    그 내용을 유추하기 어렵지만 슬러그를 사용하면 보통의 단어들이라서 이해하기 쉽기 때문임.
    SlugField 필드의 디폴트 길이는 50이며, 해당 필드에는 인덱스가 디폴트로 생성됨.
    """

    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    # description 칼럼은 빈칸(blank)도 가능합니다.
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    # content 컬럼은 TextField를 사용했으므로 여러 줄 입력이 가능합니다.
    content = models.TextField('CONTENT')
    # create_date 컬럼은 날짜와 시간을 입력하는 DateTimeField이며, auto_now_add 속성은 객체가 생성될 때의 시각을 자동으로 기록하게 합니다.
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # modify_date 컬럼은 날짜와 시간을 입력하는 DateTimeField이며, auto_now 속성은 객체가 데이터베이스에 저장될 때의 시각을 자동으로 기록하게 합니다.
    # 즉, 객체가 변경될 때의 시각이 기록되는 것임.
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tah = TagField()

    # 필드 속성 외에 필요한 파라미터가 있으면, Meta 내부 클래스로 정의합니다.
    class Meta:
        # 테이블의 별칭을 단수와 복수로 가질 수 있는데, 단수 별칭을 'post'로 함.
        verbose_name = 'post'
        # 테이블의 복수 별칭을 'posts'로 함.
        verbose_name_plural = 'posts'
        # 데이터베이스에 저장되는 테이블 이름을 'my_post'로 지정. 이 항목을 생략하면 디폴트는 '앱명_모델클래스명을 테이블 이름으로 사용함.
        # 이름을 지정하지 않았다면 'blog_post'가 되었을 것임.
        db_table = 'my_post'
        # 모델 객체 출혁 시 'modyfy_date' 컬럼을 기준으로 내림차순으로 정렬.
        ordering = ('-modify_date',)

    # 객체의 문자열을 객체.title로 표시되도록 함.
    def __str__(self):
        return self.title

    # get_absolute_url() 메소드는 이 메소드가 정의된 객체를 지칭하는 URL을 반환.
    # 메소드 내에서는 장고의 내장 함수인 reverse()를 호출함.
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # get_previous_post() 메소드는 modify_date 컬럼을 기준으로 이전 포스트를 반환
    # 메소드 내에서는 장고의 내장 함수인 get_previous_by_modify_date()를 호출함
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # get_next_post() 메소드는 modify_date 컬럼을 기준으로 다음 포스트를 반환
    # 메소드 내에서는 장고의 내장 함수인 get_next_by_modify_date()를 호출함
    def get_next_post(self):
        return self.get_next_by_modify_date()