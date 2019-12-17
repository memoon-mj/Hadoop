# 인기가 많은 서울 안의 상권, 가게는 무엇일까?
### google map populartime data & naver blog 크롤링 & 분석
- bigdataprogramming class 프로젝트

## 사용 도구
-hadoop hdfs
-zepellin
- python

## 데이터
1. 크롤링 데이터
    - GoogleMap populartimes (Google place API 이용해 크롤링) 
    https://github.com/m-wrzr/populartimes
    populartime 데이터는 구글 맵 이용자의 위치 정보를 활용합니다. 요일, 시간대 별로 얼마나 많은 사람들이 장소에 머물렀는지에 대한 정보를 제공합니다.
    current & week populartime, timespent, 위도, 경도 데이터를 활용합니다.

    - Naver search API, 블로그

2. 공공데이터
    - 서울시 우리마을가게 상권분석 서비스
    https://golmok.seoul.go.kr/source.do
