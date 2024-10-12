# Câu 2
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

svm_model= SVC(kernel='linear')
svm_model.fit(X_train,Y_train)

Y_pred = gnb.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)
classi_report = classification_report(Y_test, Y_pred)

# In kết quả
print(f"Accuracy: {accuracy:.3f}")
print("Confusion matrix:")
print(conf_matrix)
print("Classification report:")
print(classi_report)
