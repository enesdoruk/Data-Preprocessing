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
    
#feature daki nanları bulmak    
dataset['fiyat'].value_counts(dropna=False)    


dataset['fiyat'].dropna(inplace=True)

assert dataset['fiyat'].notnull().all()


dataset['fiyat'].fillna('empty',inplace=True)
print(dataset.info())



'''
DataFrame.isna
Indicate missing values.
DataFrame.notna
Indicate existing (non-missing) values.
DataFrame.fillna
Replace missing values.
Series.dropna
Drop missing values.
Index.dropna
Drop missing indices.

'''
#2.yol

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)


yas = dataset.iloc[:,1:3]
imputer =imputer.fit(yas)
yas =imputer.transform(yas)












