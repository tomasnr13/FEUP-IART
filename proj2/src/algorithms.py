#from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors

#create model

def naiveBayes(X_train, y_train, X_test):
    classifier = MultinomialNB()
    model = classifier.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def decisionTree(X_train, y_train, X_test):
    classifier = DecisionTreeClassifier(min_samples_leaf=10)
    model = classifier.fit(X_train, y_train)

    # tree.plot_tree(classifier) 

    y_pred = model.predict(X_test)

    return y_pred 

def SVM(X_train, y_train, X_test):
    classifier = SVC()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    return y_pred

def knn(X_train, y_train, X_test):
    classifier = NearestNeighbors()
    classifier.fit(X_train, y_train)

    distances, indices = classifier.kneighbors(X_train)

    print("distances:", distances)
    print("indices:", indices)

    #y_pred = classifier.predict(X_test)

    #return y_pred
