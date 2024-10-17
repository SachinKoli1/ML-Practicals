import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,3,5,7,11])

plt.scatter(x,y)
m,b=np.polyfit(x,y,1)
plt.plot(x,m*x+b)
plt.legend()
plt.show()

# The program creates a scatter plot of the data points (x, y).
# It then fits a linear regression line to the data using np.polyfit.
# The fitted line is plotted over the scatter plot, showing the trend of the data.