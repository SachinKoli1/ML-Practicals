from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

x,y=make_blobs(n_samples=300,centers=3,n_features=2,random_state=23)

plt.scatter(x[:,0],x[:,1],c=y)
plt.show()


# this program generates a synthetic dataset with 300 samples grouped into 3 clusters,
# each represented by different colors on a 2D scatter plot. This kind of visualization
# is useful for understanding the distribution of data and for testing clustering algorithms.