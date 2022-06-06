from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def snowballStemming(tokens):
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

def lemmatizing(tokens):
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

def wordCloud(corpus):
    wordcloud = WordCloud().generate(" ".join(corpus))
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()    