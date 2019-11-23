#using NAVER search api
#https://developers.naver.com/docs/search/blog/

import requests
from urllib.parse import urlparse

client_id = "0YkwTXMasrJEfC7AEdwN"
client_secret = "5CIrKH7eZe"

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
          + "&display=" + str(display) \
          + "&start=" + str(start) # json 결과    
    result = requests.get(urlparse(url).geturl(),headers = {"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})
    return result.json()

def make_list(keyword, page):
    crawl_list = [] #BigQuery에 insert할 tuple 들어있는 list                                     
    json_obj = get_api_result(keyword,page,1)
    search_count = json_obj['display']  #검색된 blog 개수
    for i in range(search_count):
        title = json_obj["items"][i]["title"].replace("<b>","").replace("</b>","") #title에서 b태그 삭제
        postdate = json_obj["items"][i]["postdate"]              
        row = (title, postdate,"1")  #한 행
        crawl_list.append(row) 
    return crawl_list

