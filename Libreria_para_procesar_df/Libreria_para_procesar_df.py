# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
from typing import Sequence, Dict, Optional, Tuple


df = pd.read_csv('amazonFire.csv',encoding='ISO-8859-1')
nombres = df.columns.values.tolist()



def fillNan(df: pd.DataFrame, column_list: Sequence[str] ) -> pd.DataFrame:
  


tipos

df_pluviosidad = pd.DataFrame(df['state'].unique()[:5],columns=['state'])
df_pluviosidad


df_pluviosidad = pd.DataFrame(df['state'].unique()[:5],columns=['state'])
df_pluviosidad['pluviosidad'] = np.random.normal(1000,200,len(df_pluviosidad))
df_pluviosidad


df_prueba= pd.DataFrame(df['state'].unique()[:5],columns=['state'])
df_prueba


df_prueba = pd.DataFrame(df['state'].unique()[:5],columns=['state'])
df_prueba['prueba'] = np.random.normal(100,20,len(df_prueba))
df_prueba




df.shape

df_left = pd.merge(df,df_pluviosidad,on='state',how='left')
df_left = pd.merge(df_left,df_prueba,on='state',how='left')


tipos = df_left.isnull()
tipos

x = df_left.columns[df_left.isnull().any()]
x



def alvaro(df):
    
    y=df.columns[df.isnull().any()]
    return y

q = alvaro(df_left)

