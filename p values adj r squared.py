import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Social_Network_Ads.csv')

#dataset import
#seperate dependent and independent variable
#cleaning missing values
#edit categorical data
# train test split

x = dataset.iloc[:,:4].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder_x = LabelEncoder()
x[:,3] = labelencoder_x.fit_transform(x[:,3])

onehotencoder = OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()

x = x[:,1:]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#from sklearn.linear_model import LinearRegression
#
#regressor = LinearRegression()
#regressor.fit(x_train,y_train)
#
#y_pred = regressor.predict(x_test)

import statsmodels.formula.api as sm

x = np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)


#x_opt = x[:,[0,1,2,3,4,5]]
#regressor_ols= sm.OLS(endog=y,exog=x_opt).fit()
#regressor_ols.summary()

def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
x_opt = x[:, [0, 1, 2, 3, 4, 5]]
x_Modeled = backwardElimination(x_opt, SL)     
        
        

    
    
