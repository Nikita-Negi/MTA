# importing required libraries
from math import pow
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#defining figure size
plt.rcParams['figure.figsize'] = (20.0, 10.0)

# loading data
data = np.genfromtxt('headbrain.csv',delimiter=',')
print('The dimensions of the dataset are:',data.shape)
X = data[1:,2]
Y = data[1:,3]

#finding the mean of the x data and the y data
mean_x = np.mean(X)
mean_y = np.mean(Y)

# here m is the total number of values
m = len(X)

# using the formula to calculate b1 and b0
#b1= sum{(xi-xmean)(yi-ymean)}/sum{(xi-xmean)^2}
#b0=ymean-b1.xmean
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# printing coefficients b1 and b0
print('The coefficients (b1,b0) are:','(',b1,',', b0,')')
#our linear model is: brainweight=b0+b1.headsize

# plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# calculating the plottable line values of x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

#plotting regression line
plt.plot(x, y, color='#58b970', label='Regression Line')
#plotting scatter plots
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

#calculating root mean square error
#rmse=sqrt(sum{(y^i-yi)^2/m})
rmse = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    rmse += (Y[i] - y_pred) ** 2
rmse = np.sqrt(rmse/m)

#displaying mean squared error
print('Mean squared error:',pow(rmse,2))
ss_t = 0
ss_r = 0

#calculating sst and ssr values
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2

#calcualting r^2 values=1-(ssr/sst)
r2 = 1 - (ss_r/ss_t)
print('Variance score:',r2)
