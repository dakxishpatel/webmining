# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:31:44 2019

@author: pateda2
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
#from sklearn.neighbors import KNeighborsClassifier

    
#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t') 
        reviews.append(review.lower()) 
        labels.append(int(rating))
    f.close()
    return reviews,labels
    
rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')
      
#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)    
    
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data
    
#train classifier
clf = RandomForestClassifier(n_estimators=1100, criterion="entropy",max_features='log2',random_state=150,max_depth=90,min_samples_split=160)
#clf = KNeighborsClassifier()
    
#train all classifier on the same datasets
clf.fit(counts_train,labels_train)
    
#use hard voting to predict (majority voting)    
predicted= clf.predict(counts_test)

#print accuracy
print (accuracy_score(predicted,labels_test))
