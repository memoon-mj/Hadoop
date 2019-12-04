import json
import csv
import pandas as pd
from pyproj import Proj, transform
import numpy as np
import json

coord = pd.read_csv("상권_좌표.csv")
proj_UTMK = Proj(init = 'epsg:5181') #GRS80
proj_WGS84 = Proj(init = 'epsg:4326') #WGS84
def transform_GRS80_to_WGS84(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x'], df['y']), index=['x', 'y'])
def transform_GRS80_to_WGS84_1(df):
    return pd.Series(transform(proj_UTMK, proj_WGS84, df['x1'], df['y1']), index=['x1', 'y1'])


coord[['x_', 'y_']] = coord.apply(transform_GRS80_to_WGS84, axis=1)
coord[['x_1', 'y_1']] = coord.apply(transform_GRS80_to_WGS84_1, axis=1)
