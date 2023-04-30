# -*- coding: utf-8 -*-
"""Task_18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jwzFFEZTM29hUrpLfndrwboenFaKDOj4
"""

# Naive Bayes Implementation

from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Splitling data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30)

# Train the model
clf = GaussianNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

# Decision Tree Implementation

from sklearn.tree import DecisionTreeClassifier

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30)

# Train the model
clf = DecisionTreeClassifier(random_state=30)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))