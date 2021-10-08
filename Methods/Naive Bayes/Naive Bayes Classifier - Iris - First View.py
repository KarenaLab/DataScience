
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Program ---------------------------------------------------------------

print("\n ****  Naive Bayes Classifier - Iris Dataset  **** \n")

Filename = "iris.csv"
DF = pd.read_csv(Filename, sep= ",")

DF_Rows = DF.shape[0]
DF_Cols = DF.shape[1]
DF_Columns = DF.columns


# Target

Target = "species"

Data_X = DF.drop(columns= [Target])     # Feature Matrix
Data_Y = DF[Target]                     # Response Vector


# Train/Test

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Data_X, Data_Y, test_size= 0.4, random_state= 27)

Gauss_NaiveBayes = GaussianNB()
Gauss_NaiveBayes.fit(X_Train, Y_Train)

Y_Predict = Gauss_NaiveBayes.predict(X_Test)
 

# Metrics
Accuracy = metrics.accuracy_score(Y_Test, Y_Predict)*100
print(f" > Accuracy= {Accuracy:.2f}%")


# Closing

print("\n * \n")



    


