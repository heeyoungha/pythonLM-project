# 장고 설치 & hello world 띄우기
```
# 장고 설치
pip install django  
ㄴ 최신 버전의 Django와 필요한 종속성을 다운로드하고 설치

django-admin --version
ㄴ Django가 올바르게 설치되었는지 확인 

# dango 프로젝트 시작
django-admin startproject [name] [path]  
django-admin startproject pythonLM .
ㄴ 새 디렉터리가 Django 프로젝트의 기본 구조와 함께 생성

# 개발 서버를 실행
cd pythonLM 
python manage.py runserver
 
# hello world
python manage.py startapp helloapp
- helloapp/veiws.py
- pythonLM/settings.py
- pythonLM/urls.py
```
# DRF 프로젝트 초기 설정
```
# 장고 REST Framework 패키지 설치
pip install djangorestframework

# 장고 프로젝트에 Django REST Framework 을 추가 
- settings.py : INSTALLED_APPS에 "rest_framework" 추가

# app 생성
python manage.py startapp bookreview

# 뷰 작성 (FBV)
- views.py : @api_view(['GET']) 작성

# URL 연결
- urls.py : bookreview/hello_rest_api 함수 연결

# 실행
python manage.py runserver
```
