# YourHomeIsMine(네집내집) 프로젝트
<img width="234" src="https://user-images.githubusercontent.com/60570733/160076605-e13d5aae-3acd-4c33-b269-19e9ee694097.png">
YourHomeIsMine은 Airbnb를 모티브 해 공간을 임대하는 숙박 공유 서비스로 예약하기까지의 로직에 집중하여 클론코딩을 진행하였습니다. </br>
소셜 로그인, 원하는 숙소 조건 검색, 숙소 리스트 조회, 숙소 상세 페이지, 인원 선택, 예약까지 하나의 플로우를 구현했습니다.
<br><br>


### 🚀 개발 인원 및 기간
* 개발 기간 : 2022/3/14 ~ 2022/3/25 (2주간)
* 프론트엔드 3명, 백엔드 3명
    * Back-end   
        * 김기현 - Modeling, Social Login API, Room Detail API, Wishlist API
        * 김은지 - Modeling, Review API, Reservation API
        * 윤명국 - Modeling, Room List API
    * Front-end  
        * 이상민 - Room List, Footer
        * 정수인 - Room Detail, Social Login
        * 신윤숙 - Room Main, Social Login, Nav, Footer 
     * <a href="https://github.com/wecode-bootcamp-korea/30-1st-CaKoo-frontend">프론트 github 링크</a>
<br><br>


# 📍 데모 영상
![메인이랑소셜로그인](https://user-images.githubusercontent.com/60570733/160085419-a86dc448-cfd2-4f1d-a2a3-2742bbdb61d2.gif)
![리스트페이지짤](https://user-images.githubusercontent.com/60570733/160085437-c4119dd7-75cc-440d-b48e-38ebec908796.gif)
![디테일페이지](https://user-images.githubusercontent.com/60570733/160085446-1c23d680-caaa-4a81-b815-ac052b4518e7.gif)


<br><br>


# 🌷 Target site

<img width="1674" alt="스크린샷 2022-03-25 오후 4 55 35" src="https://user-images.githubusercontent.com/60570733/160078345-f4f8cd46-c001-4f92-891c-38c0dbb4c404.png" >

* ## 사이트 소개  
    <a href="https://www.airbnb.co.kr/">Airbnb</a> </br>
   독특한 숙소와 체험을 제공하는 호스트를 통해 게스트에게 진정성 있는 방식으로 세상과 만나고 교감하도록 하는 것이 목표

    한국을 넘어 세계로 세상을 만나고 교감하고 싶은 사람들이 모인 곳  

* ## 사이트 선정 이유
    * 깔끔한 UI
    * 이커머스의 기본 기능인 로그인, 회원가입, 숙소 조회, 옵션 선택, 장바구니, 예약, 마이페이지 기능을 모두 담고 있음

<br><br>


# 💡 초기기획 & ERD

## ERD

<img width="1400" alt="스크린샷 2022-03-25 오후 5 02 20" src="https://user-images.githubusercontent.com/60570733/160079346-672ac8a8-5314-4167-adb9-bc433ada24c3.png">
<a href="https://www.erdcloud.com/p/ubQyfGJ5FLKhYbRAy">Site Link</a>

<br><br>

## User flow
<img src="https://user-images.githubusercontent.com/90089275/158054162-33f65fd5-e4ca-4948-ae62-22c90769e04f.png">


## 초기기획 및 구현 목표
* 짧은 기간동안 flow에 해당하는 기능 구현을 목표
* 개발은 초기세팅부터 전부 직접 구현
* 사이트 카테고리 중 숙소 예약 기능만 구현
* 필수 구현 사항을 (소셜) 로그인, 숙소 조회, 숙소 상세페이지, 예약으로 설정 
* 한 상품에 여러 옵션(숙소 종류, 인원, 기간)이 적용될 수 있게 기획

<br><br>



# 📝 적용 기술 및 구현 기능

* ## 기술 스택
    * ### Front-end  
        <a href="#"><img src="https://img.shields.io/badge/HTML-DD4B25?style=plastic&logo=html&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/SASS-254BDD?style=plastic&logo=sass&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/javascript-EFD81D?style=plastic&logo=javascript&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/React-68D5F3?style=plastic&logo=react&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/styled components-f2af9b?style=plastic&logo=styled-components &logoColor=white"/></a>
    * ### Back-end  
        <a href="#"><img src="https://img.shields.io/badge/python-3873A9?style=plastic&logo=python&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Django-0B4B33?style=plastic&logo=django&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/MySQL-005E85?style=plastic&logo=mysql&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/bcrypt-525252?style=plastic&logo=bcrypt&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/postman-F76934?style=plastic&logo=postman&logoColor=white"/></a> <br/>
    <a href="#"><img src="https://img.shields.io/badge/docker-0040FF?style=plastic&logo=docker&logoColor=white"/></a> 
    <a href="#"><img src="https://img.shields.io/badge/AWS RDS-FF9701?style=plastic&logo=rds&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS S3-FF9701?style=plastic&logo=rds&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/AWS EC2-FF9701?style=plastic&logo=rds&logoColor=white"/></a>
    * ### Common  
        <a href="#"><img src="https://img.shields.io/badge/git-E84E32?style=plastic&logo=git&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/RESTful API-415296?style=plastic&logoColor=white"/></a>
    * ### Communication  
        <a href="#"><img src="https://img.shields.io/badge/github-1B1E23?style=plastic&logo=github&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Slack-D91D57?style=plastic&logo=slack&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Trello-2580F7?style=plastic&logo=trello&logoColor=white"/></a>
        <a href="#"><img src="https://img.shields.io/badge/Notion-F7F7F7?style=plastic&logo=notion&logoColor=black"/></a>
* ## 구현기능
    * 회원가입 / 로그인
        - 카카오톡 소셜 로그인
        - 수정
        - request.header에 담긴 token을 통해 로그인 여부를 검사
    * Room List API
        - Q를 활용해 판매 상품의 분류에 따른 filtering 적용
        - 가격, 생산 순에 따른 sorting 적용
        - pagination
    * Room Detail API
        - 상품 상세페이지에 필요한 데이터를 products와 product_size, size 테이블에서 필터링 하여 엔드 포인트로 전달
        - 필요한 옵션을 선택하여 장바구니로 저장할 수 있도록 구현
    * Wishlist API
        - 장바구니 상품 추가, 조회, 수량 수정, 선택 삭제 기능 구현
    * Reservation API
        - 장바구니에서 넘겨받은 정보를 넘겨받아 구매
        - 일련의 과정에 원자성을 부여하기 위해 transaction 사용
        - 주문 후 주문내역을 받을 수 있는 로직 구현
        - 구매 한 상품은 장바구니에서 삭제   
     * Review API
        - 장바구니에서 넘겨받은 정보를 넘겨받아 구매
        - 일련의 과정에 원자성을 부여하기 위해 transaction 사용
        - 주문 후 주문내역을 받을 수 있는 로직 구현
        - 구매 한 상품은 장바구니에서 삭제
<br><br>


## API 문서화
<img width="1144" alt="스크린샷 2022-03-25 오후 5 32 57" src="https://user-images.githubusercontent.com/60570733/160084208-f227cb40-12cb-44cc-84ff-8ec766a7a8bb.png">

* 포스트맨을 이용해 API 문서화를 진행했습니다.
* 이번 프로젝트에서 쿼리파라미터(category, check_in&out, amenity, price, guest, options, page, booking 등)로 많은 값들을 받아야했기 때문에 API 문서화가 굉장히 중요했습니다.
* 프론트엔드와 소통 시 문서를 통해 1차적으로 커뮤니케이션 비용을 줄일 수 있었습니다.
<br><br>

## Trello

<img width="1676" alt="스크린샷 2022-03-25 오후 5 31 52" src="https://user-images.githubusercontent.com/60570733/160083999-169baf7d-2f32-4543-8b84-d0d09e74b1c2.png">

* 트렐로를 이용해 모든 업무들을 세분화 시켜 하나의 티켓으로 만들었습니다.
* 팀원들과 공유해야할 내용은 공지 탭을 통해 단일화하였습니다.
* 전체 프로세스를 네 가지 카테고리로 나눠서 각각의 티켓을 과정에 따라 하나씩 이동 시키며 프로젝트의 모든 일정과 업무를 관리했습니다.
* 각자 데일리 스탠드업 미팅 로그를 작성하고 10~20분내로 짧게 진행상황 및 블로커를 점검했습니다.
* 스프린트 주기를 지켜 한 스프린트가 끝나고 회고미팅을 해 발전방향을 모색하였습니다.

<br>

# Reference
* 이 프로젝트는 [꾸까](https://kukka.kr) 사이트를 참조하여 학습목적으로 만들었습니다.
* 실수수준의 프로젝트이지만 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다

![Footer](https://capsule-render.vercel.app/api?type=waving&color=ffcc51&height=100&section=footer)


