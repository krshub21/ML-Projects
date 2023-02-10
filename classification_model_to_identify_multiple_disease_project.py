@@ -0,0 +1,88 @@
# -*- coding: utf-8 -*-
"""Classification Model to Identify Multiple Disease Project.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1YH7KNN-eLPW9e4K0Qv_aBFnxxRzcb99n
# **⭐ Classification Model to Identify Multiple Disease**
"""

# import library
import pandas as pd
import seaborn

# import data
disease = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/MultipleDiseasePrediction.csv')

# view data
disease.head()

# info of data
disease.info()

# summary statistics
disease.describe()

# check for missing value
disease.isna().sum()

# check for categories
disease.nunique()

# correlation
disease.corr()

# visualize pairplot
seaborn.pairplot(disease)

# column names
disease.columns

# define y
Y = disease['prognosis']

# define X
X = disease.iloc[:,0:132]

# split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, train_size=0.7, random_state=2529)

# verify shape
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# select model
from sklearn.ensemble import RandomForestClassifier

# train model
rfc= RandomForestClassifier()
rfc.fit(X_train,y_train)

# predict with model
y_pred=rfc.predict(X_test)

# model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# model accuracy
accuracy_score(y_pred,y_test)

# model confusion matrix
confusion_matrix(y_test, y_pred)

# model classification report
print(classification_report(y_test, y_pred))

# future prediction
data = pd.DataFrame(disease.loc[2219]).transpose()
data

# define X_new
X_new = data.iloc[:,0:132]
X_new

# predict for X_new
y_new=rfc.predict(X_new)
y_new
