import re

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer

# Cleaning and tokenizing 
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

# Non-alphabetic filtering, lowercasing, stop word removal and stemming
def porterStemming(tokens):
    corpus=[]
    ss = PorterStemmer()

    for i in range(0,len(tokens)):
        stemreview=[]
        for word in tokens[i]:
            stemreview.append(ss.stem(word))
        corpus.append(' '.join(stemreview))

    return corpus

# Transform words into features / bag of words
def vectorize(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    return X