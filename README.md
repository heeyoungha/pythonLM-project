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
