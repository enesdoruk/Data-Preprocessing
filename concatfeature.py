#data  önişlemleri için
import pandas as pd

#arraylerde işlemler yapmak için
import numpy as np


#dataseti yükledik
dataset = pd.read_csv('Social_Network_Ads.csv')


#datanın ilk 5 satırını alır
data1 = dataset.head()
# datanın son 5 satırını alır
data2 = dataset.tail()

#axis 0 dememizin nedeni satır olarak birleştirmek 
#ignore_index ise eski indeksleri yok sayar
new_data=pd.concat([data1,data2],axis=0,ignore_index=True)