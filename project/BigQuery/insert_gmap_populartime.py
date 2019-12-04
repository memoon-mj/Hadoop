import json
import csv
import pandas as pd
from pyproj import Proj, transform
import numpy as np
import json
from vincenty import vincenty
from geopy import distance
import populartimes
from google.cloud import bigquery

def insert_rows(dataset_id,table_id, rows_list):
    client = bigquery.Client(project = 'bigquery-259414')
    dataset_id = dataset_id 
    table_id = table_id
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    rows_to_insert = rows_list
    
    errors = client.insert_rows(table, rows_to_insert)
    assert errors == []

with open('TBGIS_TRDAR_RELM.json','r') as jsonfile:
    data =jsonfile.read()

jsonobj = json.loads(data)

coord = pd.read_csv("상권_좌표.csv")
proj_UTMK = Proj(init = 'epsg:5181') #GRS80
proj_WGS84 = Proj(init = 'epsg:4326') #WGS84
def transform_GRS80_to_WGS84(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x'], df['y']), index=['x', 'y'])
def transform_GRS80_to_WGS84_1(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x1'], df['y1']), index=['x1', 'y1'])

coord[['x_', 'y_']] = coord.apply(transform_GRS80_to_WGS84, axis=1)

coord[['x_1', 'y_1']] = coord.apply(transform_GRS80_to_WGS84_1, axis=1)

coord1 = coord

key = "AIzaSyDwVPAZj5rkrjGHG9vgSt4HV3GJ7xQa56I"
types = ["store","subway_station","restaurant","bakery","cafe","aquarium","liquor_store","art_gallery","bar","meal_delevery","meal_takeaway","movie_theater","museum","convenience_store","shopping_mall","supermarket","grocery_or_supermarket","university","jewelry_store","hair_care"]
time_list = ["00:00:00","01:00:00","02:00:00","03:00:00","04:00:00","05:00:00","06:00:00","07:00:00","08:00:00","09:00:00","10:00:00","11:00:00","12:00:00","13:00:00","14:00:00","15:00:00","16:00:00","17:00:00","18:00:00","19:00:00","20:00:00","21:00:00","22:00:00","23:00:00","24:00:00"]
day_of_week_list = ["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]

list1 = []
list2 = []

def getData(x,y,x1,y1):
    data =populartimes.get(key, types, (x,y),(x1,y1))
    return data

for i in range(len(coord1)):
    business_distinct_code = coord1.iloc[i]['상권_구분_코드']
    business_area_code = coord1.iloc[i]['상권_코드']
    business_area_name = coord1.iloc[i]['상권_코드_명']
    x = coord1.iloc[i]['y_']
    y = coord1.iloc[i]['x_']
    x1 = coord1.iloc[i]['y_1']
    y1 = coord1.iloc[i]['x_1']
    
    data1 = getData(x,y,x1,y1)
    
    for i in range(len(data1)):
        id = data1[i]["id"]
        store_name = data1[i]["name"]
        address = data1[i]["address"]
        lat = data1[i]["coordinates"]['lat']
        lng = data1[i]["coordinates"]['lng']
        types =data1[i]["types"]
        rating = data1[i]["rating"]
        rating_n = data1[i]["rating_n"]   
        if "time_spent" in data1[i]:
            timespent_min = data1[i]["time_spent"][0]
            timespent_max = data1[i]["time_spent"][1]
        else:
            timespent_min = 0
            timespent_max = 0        
        t1 = (business_distinct_code, str(business_area_code),business_area_name,id,store_name, address, lng, lat, types, rating, rating_n,timespent_min, timespent_max)
        list1.append(t1)

        for i in range(7):
            dayofweek = day_of_week_list[i]
            for j in range(24):
                hour = time_list[j]
                t2 = (business_distinct_code, str(business_area_code),id,dayofweek, hour, data1[0]["populartimes"][i]["data"][j])
                list2.append(t2)

insert_rows('gmap_populartime','store_info',list1)
insert_rows('gmap_populartime', 'populartime_data',list2)