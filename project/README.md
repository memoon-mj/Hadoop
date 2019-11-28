# 플레이스 추천 서비스 
### SNS에서 등장 빈도수가 높은 키워드를 이용해 플레이스를 추천합니다. 
- bigdataprogramming class 프로젝트

## 사용 도구
- Google Bigquery
- Apache Airflow
- Apache zeppelin
- python

## 데이터
1. 크롤링 데이터
    - GoogleMap populartimes (Google place API 이용해 크롤링) 
    https://github.com/m-wrzr/populartimes
    - Naver DataLab API, 통합 검색어 트렌드
    https://developers.naver.com/docs/datalab/search/#%ED%86%B5%ED%95%A9-%EA%B2%80%EC%83%89%EC%96%B4-%ED%8A%B8%EB%A0%8C%EB%93%9C-api-%EB%A0%88%ED%8D%BC%EB%9F%B0%EC%8A%A4


2. 공공데이터
    - 서울시 우리마을가게 상권분석 서비스
    https://golmok.seoul.go.kr/source.do
        - (상권영역)
        - (상권-추정매출)_2019_1분기
        - 지리 정보, http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-15560&srvType=S&serviceKind=1&currentPageNo=1



## 과정
1. 분석 주제 선정, 기획
2. 데이터 수집 계획
3. 데이터 crawling
4. scheduling
5. airflow
6. zeppelin