from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

X,y=make_circles(n_samples=200,shuffle=True,noise=0.1,random_state=42)

plt.scatter(X[:,0],X[:,1],c=y)
plt.show()


# This program is generating a synthetic dataset using make_circles from the sklearn.datasets module and visualizing it using matplotlib
# This code will generate a plot where:
# The data points are arranged in two concentric circles.
# One circle will be labeled as class 0 (e.g., the inner circle) and the other as class 1 (the outer circle), with each class shown in a different color.
# classification is used for predicting the classes


# Another program
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_circles
# from sklearn.svm import SVC
# X, y = make_circles(n_samples=100, noise=0.05, factor=0.5)
# model = SVC(kernel='rbf', gamma=1.0)
# model.fit(X, y)
# xx, yy = np.meshgrid(np.linspace(X[:, 0].min()-0.5, X[:, 0].max()+0.5, 100),
#                      np.linspace(X[:, 1].min()-0.5, X[:, 1].max()+0.5, 100))
# Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
# plt.title("Support vector machine")
# plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
# plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
# plt.show()