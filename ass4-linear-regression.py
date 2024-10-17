import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
w=[2,3,5,7,11]

slop,intercept,r,p,error=stats.linregress(x,w)

def fun(x):
    return slop*x+intercept;

model=list(map(fun,x))

plt.scatter(x,w)
plt.plot(x,model)
plt.show()

# Regression
# The term regression is used when you try to find the relationship between variables.

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.

# Create the arrays that represent the values of the x and y axis:

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed:

# def myfunc(x):
#   return slope * x + intercept

# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:

# mymodel = list(map(myfunc, x))

# Draw the original scatter plot:

# plt.scatter(x, y)

# Draw the line of linear regression:

# plt.plot(x, mymodel)

# Display the diagram:

# plt.show()


