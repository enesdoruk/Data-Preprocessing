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
    

x = dataset.iloc[:,0:1] 
x=x.tail()   

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
x=lb.fit_transform(x)