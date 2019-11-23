#using NAVER datalab api
#https://developers.naver.com/docs/datalab/search/

import os
import sys
import urllib.request
import json

client_id = "0YkwTXMasrJEfC7AEdwN"
client_secret = "5CIrKH7eZe"

def get_api_result():
    url = "https://openapi.naver.com/v1/datalab/search"
    #2017/1/1 ~2017/4/30까지 연남동, 홍대를 검색어로 하고 10대~30대가 모바일, PC환경에서 검색한 빈도의 월별 상대적 변화.
    #FROM DATALAB-그래프는 네이버에서 해당 검색어가 검색된 횟수를 기간별 각각 합산하여 조회기간 내 최다 검색량을 100으로 설정하여 상대적인 변화를 나타냅니다.
    body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"연남동\",\"keywords\":[\"연남동 맛집\",\"연남동 데이트\"]},{\"groupName\":\"홍대입구\",\"keywords\":[\"홍대입구역\",\"홍대 맛집\"]}],\"ages\":[\"3\",\"4\",\"5\"]}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    response_body = response.read()
    return response_body.decode('utf-8')

def make_list():
    json_obj = get_api_result()
    json_obj = json.loads(json_obj) #json으로 변환
    crawl_list = []                 #BigQuery에 insert할 tuple 들어있는 list
    search_count = len(json_obj["results"])         #title 개수
    date_count = len(json_obj["results"][0]["data"]) #총 date 수
    for i in range(search_count):
        for j in range(date_count):
            title = json_obj["results"][i]["title"]
            date =json_obj["results"][i]["data"][j]["period"]
            ratio = json_obj["results"][i]["data"][j]["ratio"]
            row = (title, date, float(ratio)) 
            crawl_list.append(row) #한 행
    return crawl_list

print(make_list())


