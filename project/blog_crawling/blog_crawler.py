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

def call_and_print(keyword, page):
    data1 = ""

    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "")
        data = title + " " + item['postdate']
        data1 += data + "\n"
    return data1

