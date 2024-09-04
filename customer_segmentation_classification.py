# -*- coding: utf-8 -*-
"""Customer Segmentation - Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hR-nOBJRNThc4-2jel9bnQJUAFlWU6so
"""

import pandas as pd
import numpy as np

df1=pd.read_csv("/content/drive/MyDrive/datasets/Customer_Sgementation_Classification_dataset/Train.csv")
df2=pd.read_csv("/content/drive/MyDrive/datasets/Customer_Sgementation_Classification_dataset/Test.csv")

df=pd.concat([df1, df2], ignore_index=True)

df

df=df.drop("ID",axis=1)
df=df.drop("Var_1",axis=1)

df

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
a=["Gender","Ever_Married","Graduated","Profession","Spending_Score"]
for i in a:
  df[i]=le.fit_transform(df[i])
print(df)

df.isna().sum()

mean=df["Work_Experience"].mean()
df["Work_Experience"]=df["Work_Experience"].fillna(mean)

median=df['Family_Size'].median()
df["Family_Size"]=df["Family_Size"].fillna(median)

df

df.isna().sum()

df.dtypes

df["Segmentation"]=le.fit_transform(df["Segmentation"])

df

from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler()
Scaler.fit_transform(df)

df

from sklearn.model_selection import train_test_split
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X_scaled=Scaler.fit_transform(X)

y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.3,random_state=1)

from sklearn.metrics import classification_report,ConfusionMatrixDisplay,accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
knn=KNeighborsClassifier()
svc=SVC()
rf=RandomForestClassifier()
dt=DecisionTreeClassifier()
a=[knn,svc,rf,dt]
for i in a:
  i.fit(X_train,y_train)
  y_pred_i=i.predict(X_test)
  print(i)
  print(accuracy_score(y_test,y_pred_i)*100)
  print(classification_report(y_test,y_pred_i))
  print(ConfusionMatrixDisplay.from_predictions(y_test,y_pred_i))

a=int(input("enter the value for gender"))
b=int(input("enter the value for ever married"))
b1=int(input("enter the value for age"))
c=int(input("enter the value for graduated"))
d=int(input("enter the value for profession"))
e=int(input("enter the value for spending score"))
g=float(input("enter the value for work experience"))
h=float(input("enter the value for family size"))

y_pred=rf.predict([[a,b,b1,c,d,e,g,h]])
print("the customer_segment belongs to",le.inverse_transform(y_pred))

