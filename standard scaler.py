#data  önişlemleri için
import pandas as pd

#arraylerde işlemler yapmak için
import numpy as np


#dataseti yükledik
dataset = pd.read_csv('Social_Network_Ads.csv')

#id numarası gereksiz olduğu için atıyoruz

dataset =dataset.drop(['User ID'],axis=1)

#editting column name

dataset.rename(columns={'Gender':'cinsiyet','Age':'yas','EstimatedSalary':
    'fiyat','Purchased':'satis'},inplace=True)
    
    
    
x= dataset.iloc[:,1:3]
x =x.tail()
    
from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
x=sc.fit_transform(x)

