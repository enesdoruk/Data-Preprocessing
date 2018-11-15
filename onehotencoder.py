#data  önişlemleri için
import pandas as pd

#arraylerde işlemler yapmak için
import numpy as np


#3 değişkenli işlemlerde 1,0,0-0,1,0-0,0,1 i 2 sütüna düşürür
from sklearn.preprocessing import OneHotEncoder

ohe= OneHotEncoder()

x  =ohe.fit_transform(x)