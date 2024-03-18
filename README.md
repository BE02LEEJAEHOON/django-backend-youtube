# 1일차
## 프로젝트 세팅
### 1. Github
- 레포지토리 생성
- 로컬에 있는 내 컴퓨터 폴더와 github의 remote 공간 연결 진행

### 2. Docker Hub
- 회원가입 진행
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis 등))
- AccessToken 값을 Github 레포지토리에 등록 => 빌드목적

### 3. 프로젝트 세팅 (장고)
- 실제 배포 환경
- requirements.txt => 실제 배포할 때 사용
- requirements.dev.txt => 개발하고 연습할 때 사용(파이썬 패키지 관리) 테스트 많이 해보면댐 이걸로
- 실전 : 패키지 의존성 관리 (의존성 관리란 버전관리, 패키지들의 간의 관계를 말한다)


주말 공부 ㄷ ㄷ
- 도커 배운 것 정리
- 유튜브 데이터베이스 모델 구조 고민해오기
    - user : username(charfield)
    - 좋댓구알은 어케 설정하지?


## Youtube API 개발
### 1. 모델(테이블) 구조

(1) users
- email
- nickname
- password
- is_bussiness : personal, bussiness




(2) Video
- title
- description
- link
- category
- views_count
- thumbnail


- User : FK

(3) Reaction
- User : FK
- Video : FK
- reaction (like, dislike, cancel)

<!-- (4) Notifications (알림) 일단 패스
- User : FK -> 
User:Notification -> 1:N 관계 (FK는 User가 갖는다)
User -> Noti, Noti, Noti (O)
Noti ->  User, User, User(X)
- Video : FK -->

(5) Comment
- User : FK
- Video : FK
- content
- like , dislike

(6) Subscription (채널 구독 관련)
- User : FK -> subscriber (내가 구독한 사람)
- User : FK -> subscribed_to (나를 구독한 사람)


(7) Common
- created_at
- updated_at

### 본격적으로 만들어야 하는 테이블(모델)
- users, videos, reactions, comments, subscriptions, common
- docker-compose run --rm app sh -c 'python manage.py startapp users'
- docker-compose run --rm app sh -c 'python manage.py startapp videos'
- docker-compose run --rm app sh -c 'python manage.py startapp reactions'
- docker-compose run --rm app sh -c 'python manage.py startapp comments'
- docker-compose run --rm app sh -c 'python manage.py startapp subscriptions'
- docker-compose run --rm app sh -c 'python manage.py startapp common'

### Custom User Model Create
- TDD => 개발 및 디버깅 시간을 단축시킬 수 있다. PDB(PYTHON Debugger)
