import pandas as pd
import re

import algorithms

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

#cleaning and tokenizing 
def pre_process(train):
    tokens=[]
    for i in range(0,train.shape[0]):
        # remove non alphabetic chars
        title = re.sub('[^a-zA-Z]', ' ', train['review_title'][i])
        review = re.sub('[^a-zA-Z]', ' ', train['review_text'][i])
        #all words to lower
        title=title.lower()
        review = review.lower()
        #remove stop words and one letter words
        reviewarr = []
        for word in title.split():
            if word not in stopwords.words('english') and len(word)>1:
                reviewarr.append(word)
        for word in review.split():
            if word not in stopwords.words('english') and len(word)>1:
                reviewarr.append(word)
        tokens.append(reviewarr)
    return tokens



#non-alphabetic filtering, lowercasing, stop word removal and stemming
def porterStemming(tokens):
    corpus=[]
    ss = PorterStemmer()

    for i in range(0,len(tokens)):
        stemreview=[]
        for word in tokens[i]:
            stemreview.append(ss.stem(word))
        corpus.append(' '.join(stemreview))

    return corpus

def wordCloud(corpus):
    wordcloud = WordCloud().generate(" ".join(corpus))
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()    

#transform words into features / bag of words
def vectorize(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    #print(vectorizer.get_feature_names())
    return X

#performance results
def evaluatePerformance(y_test, y_pred):
    print(confusion_matrix(y_test, y_pred))
    print('Accuracy: ', accuracy_score(y_test, y_pred))
    print('Precision: ', precision_score(y_test, y_pred, average='macro'))
    print('Recall: ', recall_score(y_test, y_pred, average='macro'))
    print('F1: ', f1_score(y_test, y_pred, average='macro'))

if __name__ == "__main__":
    print("Choose the model to apply:")
    print(" 1. Naive Bayes (Multinomial)")
    print(" 2. Decision Tree")
    print(" 3. SVM")

    algorithm = int(input("Algorithm number: "))

    train = pd.read_csv("./resources/train.csv")
    test = pd.read_csv("./resources/test.csv")

    tokens= pre_process(train)
    corpus = porterStemming(tokens)
    #wordCloud(corpus)

    X = vectorize(corpus)
    y = train['class_index']

    # print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    print("\nLabel distribution in the training set:")
    print(y_train.value_counts())

    print("\nLabel distribution in the test set:")
    print(y_test.value_counts())

    if(algorithm == 1):
        ## Naive Bayes
        print("\n-------------------------")
        print(" Multinomial Naive Bayes")
        print("-------------------------")

        y_pred = algorithms.naiveBayes(X_train, y_train, X_test)
    
        print("  Performance:")
        evaluatePerformance(y_test, y_pred)
    elif algorithm==2:
        ## Decision Tree
        # better with train_big
        print("\n-------------------------")
        print("      Decision Tree")
        print("-------------------------")

        y_pred = algorithms.decisionTree(X_train, y_train, X_test)

        print("  Performance:")
        evaluatePerformance(y_test, y_pred)
    elif algorithm==3:
        ## SVM
        print("\n-------------------------")
        print("          SVM")
        print("-------------------------")

        y_pred = algorithms.SVM(X_train, y_train, X_test)

        print("  Performance:")
        evaluatePerformance(y_test, y_pred)

        # from sklearn.svm import SVC
        # from sklearn.model_selection import cross_val_score

        # clf = SVC()
        # scores = cross_val_score(clf, X, y, cv=10)

        # print(scores)
        # print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))



    ## KNN
    print("\n-------------------------")
    print("          KNN")
    print("-------------------------")

    knn = algorithms.knn(X_train, y_train)




