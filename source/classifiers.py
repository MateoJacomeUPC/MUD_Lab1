from sklearn.naive_bayes import MultinomialNB
from utils import toNumpyArray
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import LinearSVC
from sklearn.linear_model import RidgeClassifier

# You may add more classifier methods replicating this function
def applyNaiveBayes(X_train, y_train, X_test):
    '''
    Task: Given some features train a Naive Bayes classifier
          and return its predictions over a test set
    Input; X_train -> Train features
           y_train -> Train_labels
           X_test -> Test features 
    Output: y_predict -> Predictions over the test set
    '''
    trainArray = toNumpyArray(X_train)
    testArray = toNumpyArray(X_test)
    
    clf = MultinomialNB()
    clf.fit(trainArray, y_train)
    y_predict = clf.predict(testArray)
    return y_predict

def applyLDA(X_train, y_train, X_test):
      trainArray = toNumpyArray(X_train)
      testArray = toNumpyArray(X_test)
    
      clf = LinearDiscriminantAnalysis()
      clf.fit(trainArray, y_train)
      y_predict = clf.predict(testArray)
      return y_predict


def applyLSVM(X_train, y_train, X_test):
      trainArray = toNumpyArray(X_train)
      testArray = toNumpyArray(X_test)
    
      clf = LinearSVC()
      clf.fit(trainArray, y_train)
      y_predict = clf.predict(testArray)
      return y_predict
      
def applyRidge(X_train, y_train, X_test):
      trainArray = toNumpyArray(X_train)
      testArray = toNumpyArray(X_test)
    
      clf = RidgeClassifier()
      clf.fit(trainArray, y_train)
      y_predict = clf.predict(testArray)
      return y_predict
