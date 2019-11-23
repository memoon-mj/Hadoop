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
    list1 = []
    json_obj = get_api_result(keyword,page,1)
    count = json_obj['display']
    for i in range(count):
        title = json_obj["items"][i]["title"].replace("<b>","").replace("</b>","")
        postdate = json_obj["items"][i]["postdate"]
        row = (title, postdate,"1")
        list1.append(row)
    return list1

#형태소 분석



#make_list("데이트",10))
