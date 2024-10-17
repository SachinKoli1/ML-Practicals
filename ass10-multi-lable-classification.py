from sklearn.datasets import make_multilabel_classification
import matplotlib.pyplot as plt

x,y=make_multilabel_classification(n_samples=300,n_features=3,n_classes=3,random_state=42)

plt.scatter(x[:,0],x[:,1],c=y)
plt.show()


# The program generates a multi-label dataset with 3 features and 3 possible
# labels and attempts to visualize the first two features using a scatter plot