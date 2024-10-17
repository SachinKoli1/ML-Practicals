import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([120,100,80,60,40])

slop,intercept,r,p,std_error=stats.linregress(x,y)

def fun(x):
    return slop*x+intercept

model=fun(5)

print(f'The 5 Years Old Car Speed is: {model} km/h ')

plt.scatter(x,y)
plt.plot(x,fun(x))
plt.show()

