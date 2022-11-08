# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:24:22 2022

@author: User
"""

import pandas as pd
import pyarrow as py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import pickle
import gzip



def predict_ans(file_name):
    data_pred = pd.DataFrame(file_name)
    data_pred = data_pred.T
    
    columns = ['Year', 'Quarter', 'Month', 'DayofMonth', 'DayOfWeek',
           'IATA_Code_Marketing_Airline', 'Origin', 'Dest', 'CRSDepTime',
           'CRSArrTime', 'DistanceGroup',
           
           'AWND_x', 'PRCP_x', 'TMAX_x', 'TMIN_x', 'WSF2_x',
           'WSF5_x', 'SNOW_x', 'WT01_x', 'WT02_x', 'WT03_x', 'WT04_x', 'WT05_x',
           'WT06_x', 'WT07_x', 'WT08_x', 'WT09_x', 'WT10_x', 'WT11_x', 'WT18_x',
           
           'AWND_y', 'PRCP_y', 'TMAX_y', 'TMIN_y', 'WSF2_y', 
           'WSF5_y', 'SNOW_y','WT01_y', 'WT02_y', 'WT03_y', 'WT04_y', 'WT05_y', 
           'WT06_y', 'WT07_y','WT08_y', 'WT09_y', 'WT10_y', 'WT11_y', 'WT18_y',
           ]
    
    col_dict = {}
    for i in range(len(columns)):
        col_dict[i]=columns[i]
        
    data_pred.rename(columns=col_dict,inplace=True)
    print(data_pred)

    data_pred.reset_index(drop=True,inplace=True)
 
    data_pred['WTSUMx'] = (data_pred['WT01_x']+data_pred['WT02_x']+data_pred['WT03_x']+data_pred['WT04_x']+
                           data_pred['WT05_x']+data_pred['WT06_x']+data_pred['WT07_x']+data_pred['WT08_x']+
                           data_pred['WT09_x']+data_pred['WT10_x']+data_pred['WT11_x']+data_pred['WT18_x'])
    
    data_pred['WTSUMy'] = (data_pred['WT01_y']+data_pred['WT02_y']+data_pred['WT03_y']+data_pred['WT04_y']+
                           data_pred['WT05_y']+data_pred['WT06_y']+data_pred['WT07_y']+data_pred['WT08_y']+
                           data_pred['WT09_y']+data_pred['WT10_y']+data_pred['WT11_y']+data_pred['WT18_y'])


    # 將 index 整理好
    data_pred.reset_index(drop=True,inplace=True)

    # 使用者匯入資料的時候，並不會有 "WTSUMx","WTSUMy" 這兩個特徵欄位，所以在這邊加入新特徵
    data_pred['WTSUMx'] = (data_pred['WT01_x']+data_pred['WT02_x']+data_pred['WT03_x']+data_pred['WT04_x']+
                        data_pred['WT05_x']+data_pred['WT06_x']+data_pred['WT07_x']+data_pred['WT08_x']+
                        data_pred['WT09_x']+data_pred['WT10_x']+data_pred['WT11_x']+data_pred['WT18_x'])

    data_pred['WTSUMy'] = (data_pred['WT01_y']+data_pred['WT02_y']+data_pred['WT03_y']+data_pred['WT04_y']+
                        data_pred['WT05_y']+data_pred['WT06_y']+data_pred['WT07_y']+data_pred['WT08_y']+
                        data_pred['WT09_y']+data_pred['WT10_y']+data_pred['WT11_y']+data_pred['WT18_y'])


    if data_pred['WTSUMx'][0] == 0 or data_pred['WTSUMx'][0] == 1:
        df_pred = 0
    elif data_pred['WTSUMx'][0] == 2:
        df_pred = 1
    elif data_pred['WTSUMx'][0] == 3:
        df_pred = 2
    elif data_pred['WTSUMx'][0] == 4:
        df_pred = 3
    elif data_pred['WTSUMx'][0] == 5:
        df_pred = 4
    elif data_pred['WTSUMx'][0] == 6:
        df_pred = 5
    elif data_pred['WTSUMx'][0] >= 7:
        df_pred = 6    

    df_pred = pd.DataFrame([df_pred])
    return df_pred