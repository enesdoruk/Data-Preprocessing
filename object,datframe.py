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
    
#dataframe    
x=dataset.iloc[:,0:2]

#object oldu
w=dataset.iloc[:,0:2].values

#series 
y=dataset.iloc[:,3]

#integer oldu
z=dataset.iloc[:,3].values
#dataframe e cevirdik
q =pd.DataFrame(z)

