#importin load_iris function from datasets module
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
#mydata = pd.read_csv('iris.csv')
#save "bunch" object containing iris dataset and its attributes
iris = load_iris()

#store feature matrix in "X"
X = iris.data

#store respons vector in "y"
y = iris.target
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
#predicting
knn.predict([[3, 5, 4, 2], [5, 4, 3, 2]])

#testing of LogisticRegression

#import the class
#from sklearn.linear_model import LogisticRegression

#instance the model (using the defaolt parameter)
#logreg = LogisticRegression()

#fit the model with data
#logreg.fit(X, y)

#predict the response for new observations 
#y_pred = logreg.predict(X)
#print(y_pred)

# check how many predictions were generated
#len(y_pred)
#from sklearn import metrics
#print(metrics.accuracy_score(y, y_pred))