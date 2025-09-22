# 📘 PythonLM 성장 로드맵

이 프로젝트는 **Django + DRF + React/Next.js** 기반으로, 단계별로 기능을 확장하며 학습과 실습을 병행하는 로드맵을 따릅니다.  
프로젝트는 각 단계별 별도의 브랜치로 기능을 확장하며, 학습 내용을 정리하는 방식으로 진행됩니다.

이 프로젝트가 지향하는 서비스 화면 예시입니다.
<img width="1023" height="779" alt="Image" src="https://github.com/user-attachments/assets/19b53230-ebe6-4dbb-9f79-8639571a2c5c" />

---

## 🚀 Step 1  
> (작성 예정)  

---

## 🚀 Step 2 — Django & React 기본기 다지기  
**목표:** Django 설치, REST API 기본 패턴, React(Next.js) 초기화  

- Django 설치 및 Hello World 출력  
- Django REST Framework 초기 세팅  
- `bookreview` 앱 생성 → 기본 CRUD API 작성  
- Next.js 프로젝트 초기화 → `index.js` 페이지 생성  
- 독후감 게시판(Bookclub) 모델 + API 구축  

➡️ [step2 브랜치 README](../../tree/step2/README.md)

---

## 🚀 Step 3 — JazzClub 감상문 시스템 확장  
**목표:** 복잡한 관계형 데이터 모델 + 고급 DRF 패턴 활용  

- Artist / Song / SongReview 3개 모델 설계 (ERD 기반)  
- JSONField로 역할별 아티스트 관리 (보컬, 작곡, 작사, 연주자)  
- 고급 Serializer 패턴 적용: Nested, MethodField, 통합 Serializer  
- 커스텀 create/update 로직 → 통합 폼 시스템 구현  
- 아티스트 검색 API (Q 객체 + JSONField contains 활용)  
- 소프트 삭제(`deleted_at`) 적용  
- 쿼리 최적화 (select_related, 필터링)  

➡️ [step3 브랜치 README](../../tree/step3/README.md)

---

## 🌱 앞으로의 계획  
- Step 4: 인증 & 권한 관리 (JWT / OAuth2) + 테스트  
- Step 5: 배포 환경 (Docker, Nginx, CI/CD)  
- Step 6: 대규모 데이터 최적화  
- Step 7: 실서비스 적용  
