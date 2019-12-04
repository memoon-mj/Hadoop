import json
import csv
import pandas as pd
from pyproj import Proj, transform
import numpy as np
import json


proj_UTMK = Proj(init = 'epsg:5181') #GRS80
proj_WGS84 = Proj(init = 'epsg:4326') #WGS84
def transform_GRS80_to_WGS84(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x'], df['y']), index=['x', 'y'])
def transform_GRS80_to_WGS84_1(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x1'], df['y1']), index=['x1', 'y1'])

with open('TBGIS_TRDAR_RELM.json','r') as jsonfile:
    data =jsonfile.read()

jsonobj = json.loads(data)
coord = pd.read_csv("상권_좌표.csv")

count = len(jsonobj["features"])
f = open('상권_좌표1.csv', 'w', encoding ='utf-8')
wr = csv.writer(f)
for i in range(count):
    상권_구분_코드=jsonobj["features"][i]["properties"]['TRDAR_SE_C']
    상권_코드=jsonobj["features"][i]["properties"]['TRDAR_CD']
    상권_코드_명 = jsonobj["features"][i]["properties"]['TRDAR_CD_N']
    상권_구분_코드_명 =jsonobj["features"][i]["properties"]['TRDAR_SE_1']
    if(jsonobj["features"][i]["geometry"]['type'] == 'Polygon'):
        x=jsonobj["features"][i]["geometry"]["coordinates"][0][1][0]
        y=jsonobj["features"][i]["geometry"]["coordinates"][0][1][1]
        x1=jsonobj["features"][i]["geometry"]["coordinates"][0][-2][0]
        y1=jsonobj["features"][i]["geometry"]["coordinates"][0][-2][1]
       
    else:
        x=jsonobj["features"][i]["geometry"]["coordinates"][0][0][1][0]
        y=jsonobj["features"][i]["geometry"]["coordinates"][0][0][1][1]
        x1=jsonobj["features"][i]["geometry"]["coordinates"][0][0][-2][0]
        y1=jsonobj["features"][i]["geometry"]["coordinates"][0][0][-2][1]


    coord[['x_', 'y_']] = coord.apply(transform_GRS80_to_WGS84, axis=1)
    coord[['x_1', 'y_1']] = coord.apply(transform_GRS80_to_WGS84_1, axis=1)
   
    insert_row = [상권_구분_코드,상권_코드,상권_코드_명,상권_구분_코드_명,x,y,x1,y1,x_,y_,x_1,y_1]
    wr.writerow(insert_row)
f.close()


