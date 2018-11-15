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
  
    
#x ve y diye böldük    
x = dataset.iloc[:,[0,1,2]]
y = dataset.iloc[:,3].values

# train,test diye bölüyoruz bu kütüphane ile random yapabiliyoruz ve bölme 
#oranını veriyoruz    
from sklearn.cross_validation import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)    