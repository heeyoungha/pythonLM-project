# 장고 설치 & hello world 띄우기

## 📁 프로젝트 구조
```
pythonLM/ (프로젝트 루트)
├── 📁 .git/                    # Git 저장소
├── 📄 .gitignore              # Git 무시 파일
├── 📁 .venv/                  # Python 가상환경
└── 📁 pythonLM/               # 메인 프로젝트 폴더
    ├── 📄 README.md           # 프로젝트 문서
    ├── 📁 backend/            # Django 백엔드
    │   ├── 📁 bookreview/     # Django 앱 (REST API)
    │   ├── 📁 helloapp/       # Django 앱 (Hello World)
    │   ├── 📁 pythonLM/       # Django 설정
    │   ├── 📄 manage.py       # Django 관리 스크립트
    │   └── 📄 db.sqlite3      # 데이터베이스
    └── 📁 frontend/           # Next.js 프론트엔드
        ├── 📁 pages/          # Next.js 페이지들
        ├── 📁 src/            # React 컴포넌트들
        ├── 📁 public/         # 정적 파일들
        ├── 📄 package.json    # Node.js 의존성
        └── 📁 node_modules/   # Node.js 패키지들
```

```
# 장고 설치
pip install django  
ㄴ 최신 버전의 Django와 필요한 종속성을 다운로드하고 설치

django-admin --version
ㄴ Django가 올바르게 설치되었는지 확인 

# dango 프로젝트 시작
django-admin startproject [name] [path]  
django-admin startproject pythonLM backend
ㄴ backend 폴더에 Django 프로젝트 생성

# 개발 서버를 실행
cd pythonLM/backend
python manage.py runserver
 
# hello world
python manage.py startapp helloapp
- helloapp/views.py
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

# React 프로젝트 초기화 
```
# frontend 폴더 생성
mkdir -p frontend
cd frontend

# Next.js 프로젝트 초기화
npm init -y
npm install next react react-dom

# package.json scripts 수정
- "dev": "next dev"
- "build": "next build"
- "start": "next start"

# pages 폴더 생성
mkdir pages
cd pages
touch index.js
```
