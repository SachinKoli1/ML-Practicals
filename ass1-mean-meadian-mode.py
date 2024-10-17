import numpy as np
from scipy import stats

x=[99,86,87,88,111,86,103,87,94,78,77,85,86]
a=np.mean(x)
print(a)
b=np.median(x)
print(b)
c=stats.mode(x)
print(c)


# Mean - The average value
# Median - The mid point value
# Mode - The most common value