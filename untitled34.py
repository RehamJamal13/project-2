# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15ZlSiobOwWmeZJY66nxPOvsnfq6Nav1q
"""

# Commented out IPython magic to ensure Python compatibility.
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,mean_squared_error
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

!ls /content/drive/My\ Drive/

import pandas as pd
file_path = '/content/drive/My Drive /default_of_credit_card_clients.csv'
df1 = pd.read_csv(file_path,skiprows=1)
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')
#df = df1.drop(df1.index[0])

print(df1.head())



df1.describe().T

df1.rename(columns={'default payment next month':'def_pay'}, inplace=True)

df1.isna().sum()

plt.subplots(figsize=(20,5))
plt.subplot(121)
sns.distplot(df1.LIMIT_BAL)

plt.subplot(122)
sns.distplot(df1.AGE)

plt.show()

bins = [20,30,40,50,60,70,80]
names = ['21-30','31-40','41-50','51-60','61-70','71-80']
df1['AGE_BIN'] = pd.cut(x=df1.AGE, bins=bins, labels=names, right=True)

age_cnt = df1.AGE_BIN.value_counts()
age_0 = (df1.AGE_BIN[df1['def_pay'] == 0].value_counts())
age_1 = (df1.AGE_BIN[df1['def_pay'] == 1].value_counts())

plt.subplots(figsize=(8,5))
# sns.barplot(data=df1, x='AGE_BIN', y='LIMIT_BAL', hue='def_pay', ci=0)
plt.bar(age_0.index, age_0.values, label='0')
plt.bar(age_1.index, age_1.values, label='1')
for x,y in zip(names,age_0):
    plt.text(x,y,y,fontsize=12)
for x,y in zip(names,age_1):
    plt.text(x,y,y,fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Number of clients in each age group", fontsize=15)
plt.legend(loc='upper right', fontsize=15)
plt.show()

df_X = df1.drop(['def_pay','AGE_BIN'], axis=1)
df_y = df1.def_pay

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=10)

model1 = LogisticRegression()
model1.fit(X_train, y_train)

y_pred = model1.predict(X_test)

print(classification_report(y_pred, y_test))
print(confusion_matrix(y_pred, y_test))
print('\nAccuracy Score for model1: ', accuracy_score(y_pred,y_test))

import joblib

# Save the trained model
joblib.dump(model1, 'logistic_regression_model.pkl')

# Load the model from the saved file
model1 = joblib.load('logistic_regression_model.pkl')

# Make predictions
y_pred = model1.predict(X_test)

