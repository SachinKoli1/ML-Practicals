from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Loading the Iris Dataset
iris=load_iris()
x,y=iris.data,iris.target

#  Splitting the Data into Training and Testing Sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#  Creating and Training the KNN Classifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

#  Creating and Training the KNN Classifier
y_pred=knn.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy {accuracy*100}% ")


# Output:
# The accuracy value will tell you how well the KNN 
# classifier performed on the test set. The higher 
# the accuracy, the better the classifier was at 
# correctly predicting the species of the Iris flowers.