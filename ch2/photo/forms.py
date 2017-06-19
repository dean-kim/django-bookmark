# -*- coding: utf-8 -*-

# 폼셋에 필요한 모델을 임포트
from photo.models import Album, Photo

# 인라인 폼셋을 반환하는 inlineformset_factory() 함수를 임포트
from django.forms.models import inlineformset_factory

# 1:N 관계인 Album과 Photo 테이블을 이용해 사진 인라인 폼셋을 만듭니다.
PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           # 사진 모델에서 폼셋에 사용하는 필드를 지정
                                           fields = ['image', 'title', 'description'],
                                           # 폼셋에 들어 있는 빈 폼의 개수는 2개로 지정
                                           extra = 2)