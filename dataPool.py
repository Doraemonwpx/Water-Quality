# python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 20:21
# @Author  : Yran CHan
# @Site    : 
# @File    : dataPool.py
# @Software: PyCharm

import os
import pandas as pd
import numpy as np

def data_preprosessing(dataPath:str, keyName:str='STATION_ID',dateName:str='SAMPLE_DATE')->pd.DataFrame:
    data_df = pd.DataFrame()
    if dataPath.endswith('csv'):
        try:
            data_df = pd.read_csv(dataPath)
        except:
            raise FileNotFoundError
    # data_df = data_df.set_index(keyName)
    data_df[dateName] = pd.to_datetime(data_df[dateName])
    return data_df

def data_time_slice(data:pd.DataFrame,startDate:str,endDate:str,dateName:str='SAMPLE_DATE'):
    return data[(data[dateName]>=startDate) & (data[dateName]<=endDate)]

def save_file(df:pd.DataFrame,savePath:str,fileName:str):
    dirName = os.path.join(savePath,fileName)
    absPath = os.path.abspath(dirName)
    if not os.path.exists(os.path.dirname(dirName)):
        os.makedirs(os.path.dirname(dirName))
    if dirName.endswith('csv'):
        df.to_csv(dirName,index=0)
        print ('File saved to: ' + absPath )

if __name__ == "__main__":

    # 数据源放在 data-forward 文件夹同一目录下
    data_path_lab = '../data/raw_data/lab_results.csv'
    data_path_field = '../data/raw_data/field_results.csv'
    save_path = '../data/clean_data'

    for p in [data_path_lab,data_path_field]:
        data = data_preprosessing(p)
        res = data_time_slice(data,'2017-01-01','2021-12-31')
        print (res[''])
        save_file(res,save_path,p.split('/')[-1])

    print(0)