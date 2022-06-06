import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import time


train = pd.read_csv("./resources/train.csv")
#test = pd.read_csv("./resources/test.csv")
tokens=[]
corpus=[]

#cleaning and tokenizing 
def pre_process():
    tokens=[]
    for i in range(0,train.shape[0]):
        # remove non alphabetic chars
        title = re.sub('[^a-zA-Z]', ' ', train['review_title'][i])
        review = re.sub('[^a-zA-Z]', ' ', train['review_text'][i])
        #all words to lower
        title=title.lower
        review = review.lower
        #remove stop words
        titlearr = []
        for word in title.split:
            if word not in stopwords.words('english'):
                titlearr.append(word)
        reviewarr = []
        for word in review.split:
            if word not in stopwords.words('english'):
                reviewarr.append(word)
        tokens.append((titlearr,reviewarr))


#stemming
def snowballStemming():
    corpus=[]
    ss = SnowballStemmer(language='english')

    for i in range(0,len(tokens)):
        stemtitle=[]
        for word in tokens[i][0]:
            stemtitle.append(ss.stem(word))
        stemreview=[]
        for word in tokens[i][1]:
            stemreview.append(ss.stem(word))
        corpus.append((' '.join(stemtitle),' '.join(stemreview)))

def porterstemming():
    corpus=[]
    ss = PorterStemmer(language='english')

    for i in range(0,len(tokens)):
        stemtitle=[]
        for word in tokens[i][0]:
            stemtitle.append(ss.stem(word))
        stemreview=[]
        for word in tokens[i][1]:
            stemreview.append(ss.stem(word))
        corpus.append((' '.join(stemtitle),' '.join(stemreview)))

#lemmatizing
def lemmatizing():
    corpus=[]
    wnl = WordNetLemmatizer()

    for i in range(0,len(tokens)):
        stemtitle=[]
        for word in tokens[i][0]:
            stemtitle.append(wnl.lemmatize(word))
        stemreview=[]
        for word in tokens[i][1]:
            stemreview.append(wnl.lemmatize(word))
        corpus.append((' '.join(stemtitle),' '.join(stemreview)))

#transform words into features / bag of words
def vectorize():
    vect = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1,2))#see if it is too much
    features = vect.fit_transform([tup[0]+tup[1] for tup in corpus]).toarray()
    #features_review = vect.fit_transform([tup[1] for tup in corpus])
    #pd.DataFrame(features_review.todense(),columns=vect.get_feature_names())


#create model

def naiveBayes(X_train, y_train, X_test):
    classifier = GaussianNB()
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
    y_pred = classifier.predict(X_test)

    return y_pred

#performance results
def evaluatePerformance(y_test, y_pred):
    print(confusion_matrix(y_test, y_pred))
    print('Accuracy: ', accuracy_score(y_test, y_pred))
    print('Precision: ', precision_score(y_test, y_pred))
    print('Recall: ', recall_score(y_test, y_pred))
    print('F1: ', f1_score(y_test, y_pred))

