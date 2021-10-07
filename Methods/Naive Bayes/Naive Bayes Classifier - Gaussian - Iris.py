
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

Sample_List = np.linspace(start= 10, stop= 60, num= 11)


Acc_Train_List = []
Acc_Test_List = []


for Sample in Sample_List:

    print(f" > Performing Gaussian Naive Bayes for Sample = {int(Sample)}%")

    Sample = Sample/100
    X_Train, X_Test, Y_Train, Y_Test = train_test_split(Data_X, Data_Y, test_size= Sample, random_state= 27)

    Gauss_NaiveBayes = GaussianNB()
    Gauss_NaiveBayes.fit(X_Train, Y_Train)

    Y_Pred_Train = Gauss_NaiveBayes.predict(X_Train)
    Y_Pred_Test = Gauss_NaiveBayes.predict(X_Test)

    # Metrics
    Acc_Train = metrics.accuracy_score(Y_Train, Y_Pred_Train)*100
    Acc_Test = metrics.accuracy_score(Y_Test, Y_Pred_Test)*100

    Acc_Train_List.append(Acc_Train)
    Acc_Test_List.append(Acc_Test)


# Plotting

plt.style.use("ekc")

fig = plt.figure()

Title = "Gaussian Naive Bayes Classifier - Iris Petals"
fig.suptitle(Title, fontsize= 14)

plt.plot(Sample_List, Acc_Train_List, color= "navy", label= "Train")
plt.plot(Sample_List, Acc_Test_List, color= "darkred", label= "Test")

plt.xlabel("% Test Size")
plt.ylabel("% Accuracy")

plt.legend(loc= "lower right")
plt.savefig(Title, dpi= 240)
plt.show()


# Closing

print("\n * \n")

