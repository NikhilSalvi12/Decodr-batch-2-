# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:00:45 2021

@author: AJ
"""

#Simple Linear Regression 
import pandas as pd
wc_at = pd.read_csv("https://raw.githubusercontent.com/THEFASHIONGEEK/DATA-SCIENCE/master/Simple%20Linear%20Regression/wc.at.csv")

wc_at.isnull().sum()

wc_at.boxplot()

#no outliers and no missing values

from sklearn.model_selection import train_test_split

train, test = train_test_split(wc_at,test_size = 0.20)

# must do for simple linear regression- transpose the data
import numpy as np
X = np.array(wc_at.Waist).reshape(-1,1)
y = np.array(wc_at.AT).reshape(-1,1)

x_train , x_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression

#to create the model
model = LinearRegression() #y = mx + C

#to train model/ fitting the model
model.fit(X = x_train,  y= y_train)

#to coeffecient of x
model.coef_

#to intercept or constant
model.intercept_

#equation of line = y = 3.5x - 221

import seaborn as sns
sns.relplot(x = "Waist",
            y = "AT",
            data = wc_at,
            kind = "scatter")

y_pred = model.predict(x_test)


y_pred_train =model.predict(x_train)

pred_value = model.predict(np.array(wc_at.Waist).reshape(-1,1))


# to find the accuracy of the model
model.score(X = x_test, y = y_test)

# model deployment
X_new = np.array([50,55,70,80]).reshape(-1,1)

y_new = model.predict(X_new)
y_new




#HW : Y = bigmart sales x = Item Weight 
#score & pred values & graph scatterplot and lineplot together over one another
#predict for Item weight -5, 10, 3.7 , 8.906
 



plt.scatter(wc_at.Waist,wc_at.AT)
plt.plot(wc_at.Waist,pred_value,"r")

plt.scatter(x_train,y_train)
plt.plot(x_train,y_pred_train,"r")

plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,"g")


plt.scatter(x_train,y_train)
plt.scatter(x_test,y_test)
plt.plot(wc_at.Waist,pred_value,"r")




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto_data = pd.read_csv("auto-mpg.data",delim_whitespace = True,names=['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','car_name'],na_values= "?")


auto_data.isnull().sum()
auto_data.info()

auto_data.horsepower.unique()

auto_data.boxplot()
auto_data.horsepower.fillna(auto_data.horsepower.median(),inplace=True)

#y - mpg
# x - cylinders, displacement, horsepower','weight','acceleration','model_year','origin'

auto_data.drop('car_name',inplace = True, axis  = 1 )

#multi linear regression y & x - (C)

y = auto_data.mpg
X = auto_data.iloc[:,1:]

#model splitting
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size =0.2,                                                   random_state = 123)

#model creation 
mul_reg = LinearRegression()

#model fitting
mul_reg.fit(X = x_train, y = y_train)

#model equation
mul_reg.coef_
mul_reg.intercept_

#model accuracy
mul_reg.score(x_test, y_test) #0.788

# 4 cars mpg
#cy = [8,6,4,6]
#dis = [500,390,440,414]
#hp = [90,110,56,70]
#wt = [3555,4321,3456,2345]
#acc = [10.5,11.2,5.6,7.9]
#yr = [70,73,75,70]
#origin = [1,1,2,3]

# to create the dataframe - Create dict first with columns names as key
to_predict = {'cylinders':[8,6,4,6],'displacement':[500,390,440,414],
              'horsepower':[90,110,56,70],'weight':[3555,4321,3456,2345],
              'acceleration':[10.5,11.2,5.6,7.9],'model_year':[70,73,75,70],
              'origin':[1,1,2,3]}

#to convert dict to dataframe
to_predict = pd.DataFrame(to_predict)

#to predict new mpg values
mul_reg.predict(to_predict)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

auto_price = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data",header =None, na_values = "?")

auto_price.columns =["symboling","normalized_losses","make","fuel_type","aspiration","num_of_doors","body_style","drive_wheels","engine_location","wheel_base","length","width","height","curb_weight","engine_type","num_of_cylinders","engine_size","fuel_system","bore","stroke","compression_ratio","horsepower","peak_rpm","city_mpg","highway_mpg","price"]

# y = price
# x = all continous data






















