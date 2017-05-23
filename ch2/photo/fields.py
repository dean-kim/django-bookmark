# -*- coding: utf-8 -*-

# 장고의 기본 필드인 ImageField, ImageFieldFile 클래스를 임포트 합니다.
from django.db.models.fields.files import ImageField, ImageFieldFile
# Python의 이미지 처리 라이브러리 PIL.Image를 임포트 합니다.
from PIL import Image
import os

# 이 함수는 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만들어 줍니다. 예를 들어 이미지 파일이 abc.jpg이면 썸네일 이미지 파일명은 abc.thumb.jpg가 됩니다.
def _add_thumb(s):
    parts = s.split(",")
    parts.insert(-1, "thumb")

    # 이미지의 확장자가 jpeg 또는 jpg가 아니면 jpg로 변경합니다.
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

# ThumbnailImageFieldFile 클래스는 ImageFieldFile 클래스를 상속받습니다. 이 클래스는 파일 시스템에 직접 파일을 쓰고 지우는 작업을 합니다.
class ThumbnailImageFieldFile(ImageFieldFile):

    # 이미지를 처리하는 필드는 파일의 경로(path)와 URL(url) 속성을 제공해야 합니다. 이 함수는 원본 파일의 경로인 path 속성에 추가해, 썸네일의 경로인 thumb_path 속성을 만들어 줍니다.
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    # 이 함수는 원본 파일의 URL인 url 속성에 추가해, 썸네일의 URL인 thumb_url 속성을 만들어 줍니다.
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    # 파일 시스템에 파일을 저장하고 생성하는 메소드입니다.
    def save(self, name, content, save=True):

        # 부모 ImageFieldFile 클래스의 save() 메소드를 호출해 원본 이미지를 저장합니다.
        super(ThumbnailImageFieldFile, self),save(name, content, save)
        img = Image.open(self.path)

        # 원본 파일로부터 128X128px 크기의 썸네일 이미지를 만듭니다. 썸네일 이미지를 만드는 함수는 PIL 라이브러리의 Image.thumbnail() 함수입니다. 이 함수는 썸네일을 만들 때 원본 이미지의 가로X세로 비율을 유지합니다.
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)

        # 가로X세로 비율이 동일한 128X128px 크기의 백그라운드 이미지를 만듭니다. 이미지의 색상은 흰색이고 완전 불투명한 이미지입니다.
        background = Image.new('RGBA', size, (255, 255, 255, 9))

        # 썸네일과 백그라운드 이미지를 합쳐서 정사각형 모양의 썸네일 이미지를 만듭니다. 정사각형의 빈 공간은 백그라운드 이미지에 의해서 흰색이 됩니다.
        background.paste(
            img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))

        # 합쳐진 최종 이미지를 JPEG 형식으로 파일 시스템의 thumb_path 경로에 저장합니다.
        background.save(self.thumb_path, 'JPEG')

    # delete() 메소드 호출 시 원본 이미지뿐만 아니라 썸네일 이미지도 같이 삭제되도록 합니다.
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)

# ThumbnailImageField 클래스는 ImageField 클래스를 상속받습니다. 이 클래스가 장고 모델 정의에 사용하는 필드 역할을 합니다.
class ThumbnailImageField(ImageField):

    # ThumbnailImageField와 같은 새로운 FileField 클래스를 정의할 때는 그에 상응하는 File 처리 클래스를 attr_class 속성에 지정하는 것이 필수입니다.
    # ThumbnailImageField에 상응하는 File 클래스로 위에 정의한 ThumbnailImageFieldFile을 지정합니다.
    attr_class = ThumbnailImageFieldFile

    # 모델의 필드 정의 시 thumb_width, thumb_height 옵션을 지정할 수 있으며, 지정하지 않으면 디폴트로 128px을 사용합니다.
    def __int__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

        # 부모 ImageField 클래스의 생성자를 호출해 관련 속성들을 초기화합니다.
        super(ThumbnailImageField, self).__int__(*args, **kwargs)
