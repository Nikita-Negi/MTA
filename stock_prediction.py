#importing necessary libraries
import pandas as pd                 #used to create dataframes
import numpy as np                  #used for mathematical functions and arrays
import quandl                       #used to load the stock data
import matplotlib.pyplot as plt     #used for plotting purposes
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm    #used for regression algorithms
import datetime                     #used for date and time functions

#data is imported using quandl to get up-to-date stock dataset of amazon
df = quandl.get("WIKI/AMZN")
print('THE USED DATASET IS AS FOLLOWS:\n',df.tail())

#out of the above data we only need the closing price of the stocks for each day, so we only use that dataframe to predict
df = df[['Adj. Close']]
#plotting the above dataframe
plt.plot(df)
plt.title('Existing prices since 1997 till today of the amazon stock (price vs time)')
plt.show()

# as we are predicting 15 days into future, we create forecast_out containing 15 integers
forecast_out = int(15)
# this the the data which is to be trained upon which is all the data except last 15 values
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

#our x data has adj.close values, so we drop the prediction column and scale the values
X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

#our forecasting data has the last 15 values of the adj.close and we remove these values from x
X_forecast = X[-forecast_out:]
X = X[:-forecast_out]

#our y is equal to the prediction values except the last 15 days for which we do not have any data
y = np.array(df['Prediction'])
y = y[:-forecast_out]

#we split our testing and training data sets, and set our test_size equal to 20% of the data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

#training the dataset
clf = LinearRegression()
clf.fit(X_train,y_train)
#testing the dataset
confidence = clf.score(X_test, y_test)          #based on r^2 value
print("\n\nCONFIDENCE/ACCURACY VALUE: ", confidence,'\n\n')

#getting the forecasted values for the next 30 days
forecast_prediction = clf.predict(X_forecast)
print('THE FORECAST OF THE STOCK PRICES FOR THE NEXT 15 DAYS ARE:\n',forecast_prediction)

#plotting the forecasted data for the next 15 days
plt.plot(forecast_prediction)
plt.title('Predicted prices for the amazon stock 15 days from today (price vs time)')
plt.show()

