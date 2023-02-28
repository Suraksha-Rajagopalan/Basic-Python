import pandas as pd
world=pd.read_csv(r'C:\Users\SUDHA\Desktop\World.csv')
y = (world.Pollution_Index)
X = world.drop(['Pollution_Index','City','Rank'],axis=1)
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

y = (world.Pollution_Index)
X = world.drop(['Pollution_Index','City','Rank'],axis=1)

# Split the data into training/testing sets
X_train = X[20:]
X_test = X[:20]

# Split the targets into training/testing sets
y_train = y[20:]
y_test = y[:20]

# Create linear regression object
regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test, y_test, alpha=0.75, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
