#using NAVER search api
#https://developers.naver.com/docs/search/blog/

import requests
from urllib.parse import urlparse

    #url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
url = "http://apis.data.go.kr/B553077/api/open/sdsc/storeZoneOne?key=573&ServiceKey=573&ServiceKey=lt0X1NwBquxQ4wP2tHL5Ze18esAgLrsG4DtP7CHhCrH%2BUES16ia5cHFju6aJZ6tFsEzZWOz0m2bCi9y5DshE%2Bg%3D%3D"
    #lt0X1NwBquxQ4wP2tHL5Ze18esAgLrsG4DtP7CHhCrH%2BUES16ia5cHFju6aJZ6tFsEzZWOz0m2bCi9y5DshE%2Bg%3D%3D
result = requests.get(url)
result.json()

