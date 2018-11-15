#data  önişlemleri için
import pandas as pd

#arraylerde işlemler yapmak için
import numpy as np


df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale':[55, 40, 84, 31]})

df.set_index('month')
df.set_index(['year', 'month'])
df.set_index([[1, 2, 3, 4], 'year'])

df.rename(index={0:'month'}, columns={1:'SM'}, inplace=True)