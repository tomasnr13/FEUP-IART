import algorithms
import eval_performance
import data_process
import time

import pandas as pd

from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    print("Choose the model to apply:")
    print(" 1. Naive Bayes (Multinomial)")
    print(" 2. Decision Tree")
    print(" 3. SVM")

    algorithm = int(input("Algorithm number: "))

    train = pd.read_csv("./resources/train.csv")
    test = pd.read_csv("./resources/test.csv")

    tokens= data_process.pre_process(train)
    corpus = data_process.porterStemming(tokens)

    X = data_process.vectorize(corpus)
    y = train['class_index']

    # print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    # print("\nLabel distribution in the training set:")
    # print(y_train.value_counts())

    # print("\nLabel distribution in the test set:")
    # print(y_test.value_counts())

    start_time = time.time()
    if(algorithm == 1):
        ## Naive Bayes
        print("\n-------------------------")
        print(" Multinomial Naive Bayes")
        print("-------------------------")

        y_pred = algorithms.naiveBayes(X_train, y_train, X_test)
    
        print("  Performance:")
        eval_performance.evaluatePerformance(y_test, y_pred)
    elif algorithm==2:
        ## Decision Tree
        # better with train_big
        print("\n-------------------------")
        print("      Decision Tree")
        print("-------------------------")

        y_pred = algorithms.decisionTree(X_train, y_train, X_test)

        print("  Performance:")
        eval_performance.evaluatePerformance(y_test, y_pred)
    elif algorithm==3:
        ## SVM
        print("\n-------------------------")
        print("          SVM")
        print("-------------------------")

        y_pred = algorithms.SVM(X_train, y_train, X_test)

        print("  Performance:")
        eval_performance.evaluatePerformance(y_test, y_pred)
    print(f'Time: {round(time.time() - start_time, 6)} seconds')
  