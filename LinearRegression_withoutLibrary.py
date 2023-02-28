import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv(r'C:\Users\SUDHA\Desktop\World.csv')
X = dataset['Pollution_Expectation'].values
Y = dataset['Pollution_Index'].values

#mean of our inputs and outputs
x_mean = np.mean(X)
y_mean = np.mean(Y)

#total number of values
n = len(X)

#using the formula to calculate the b1 and b0
numerator = 0
denominator = 0
for i in range(0,n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2
    
b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)

#printing the coefficient
print(b1, b0)
#plotting values 
x_max = np.max(X) + 100
x_min = np.min(X) - 100

#calculating line values of x and y
x = np.linspace(x_min, x_max, 100000)
y = b0 + b1 * x

#plotting line 
plt.plot(x, y, color='blue', label='Linear Regression')

#plot the data point
plt.scatter(X, Y, color='black', label='Data Point', alpha=0.75)

# x-axis label
plt.xlabel('Pollution_Expectation')

#y-axis label
plt.ylabel('Pollution_Index')

plt.legend()
plt.margins(x=-0.45, y=-0.45)
plt.show()
