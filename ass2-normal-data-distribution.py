from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000),hist=False)
plt.show()

# create an array where the values are concentrated around a given value

# Another Program
# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 100000)

# plt.hist(x, 100)
# plt.show()