import ex_crawl
loc_list =["홍대","부산","인천"]
json_obj = ex_crawl.get_api_result("데이트",5,1)
for i in range(5):
    title =json_obj["items"][0]["title"]
    #if loc_list in title: 
        #print(title)
    print(title)
