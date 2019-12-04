import populartimes

key = "AIzaSyDwVPAZj5rkrjGHG9vgSt4HV3GJ7xQa56I"
data1 =populartimes.get(key, ["restaurant","bakery","cafe"], (37.55213181853304,126.9215177589102),(37.558268, 126.925723))
#data1 = populartimes.get(key, ["restaurant","bakery","cafe"], (37.55757406448484,126.93691538021643),(37.55757406448484,126.93891538021643))

def make_list():
    list1 = []
    for i in range(len(data1)):
        name = data1[i]["name"]
        address = data1[i]["address"]
        lat = data1[i]["coordinates"]['lat']
        lng = data1[i]["coordinates"]['lng']
        types =data1[i]["types"]
        rating = data1[i]["rating"]
        rating_n = data1[i]["rating_n"]
        mon = data1[i]["populartimes"][0]["data"]
        tue = data1[i]["populartimes"][1]["data"]
        wed=data1[i]["populartimes"][2]["data"]
        thur =data1[i]["populartimes"][3]["data"]
        fri =data1[i]["populartimes"][4]["data"]
        sat = data1[i]["populartimes"][5]["data"]
        sun = data1[i]["populartimes"][6]["data"]
        t1 = (name, address, lat, lng, types, rating, rating_n, mon, tue,wed,thur, fri, sat, sun)
        list1.append(t1)
    return list1

print(make_list())