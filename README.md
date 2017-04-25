# django-bookmark
Python Django study

이 스터디는 한빛미디어 출판사의 'Django를 활용한 쉽고 빠른 웹 개발 파이썬 웹 프로그래밍의 예제를 실습한 스터디입니다.'


# 작업 순서

 ## 0. 작업 준비
   #### 0-1. Python 설치
   #### 0-2. 가상 개발환경 구축(env라는 개발환경 구축)
    pip3.4 install virtualenv
    virtualenv env
    source env/bin/activate

 ## 1. 뼈대 만들기
   #### 1-1. startproject : 프로젝트 생성
    python manage.py startproject '프로젝트명' .
   #### 1-2. settings.py : 프로젝트 설정 항목 변경
   #### 1-3. migrate : 테이블 생성
    python manage.py migrate
   #### 1-4. createsuperuser: 프로젝트 관리자인 슈퍼유저 생성
    python manage.py createsuperuser
   #### 1-5. startapp : 앱 생성
    python manage.py startapp 'app명'
   #### 1-6. settings.py : 앱 등록

 ## 2. 모델 코딩
   #### 2-1. models.py : 모델(테이블) 정의
   #### 2-2. admin.py : Admin 페이지에 모델 등록
   #### 2-3. makemigrations : 모델을 데이터베이스에 반영
    python manage.py makemigrations
   #### 2-4. migrate : 테이블 생성
    python manage.py migrate

 ## 3. URLconf 코딩
   #### 3-1. urls.py : URL 정의

 ## 4. 뷰 코딩
   #### 4-1. views.py : 뷰 로직 작성

 ## 5. 템플릿 코딩
   #### 5-1. templates 디렉토리 : 템플릿 파일 작성