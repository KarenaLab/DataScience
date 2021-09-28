
import numpy as np
import pandas as pd


# Definitions and Setup -------------------------------------------------

def Sigmoid(x):

    Sig = 1.0/(1.0 + np.exp(-x))
    return Sig


def Square_Loss(y_pred, target):

    SL = np.mean((y_pred-target)**2)
    return SL


sample = 10
threshold = 0.5



# Program ---------------------------------------------------------------

print("\n ****  Manual Logistic Regression  **** \n")


Age_List = [22, 25, 47, 52, 46, 56, 55, 60, 62, 61,
            18, 28, 27, 29, 49, 55, 25, 58, 19, 18,
            21, 26, 40, 45, 50, 54, 23, 18, 45, 69 ]

Insurance_List = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1,
                  0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
                  0, 0, 1, 1, 1, 1, 0, 0, 1, 1 ]


DF = pd.DataFrame(Age_List, columns= ["age"])
DF["insurance"] = Insurance_List


Test = DF.sample(sample)

Train = DF[~DF.isin(Test)]
Train = Train.dropna()


# Splitting

x_train = Train["age"]
y_train = Train["insurance"]

x_test = Test["age"]
y_test = Test["insurance"]


# Calculating

LR = 0.01                            # Learning Rate
B = np.random.uniform(0, 1)          # Slope
W = np.random.uniform(0, 100)        # Intercept


i = 0
while(i < 60000):

    z = np.dot(x_train, W)+B

    y_pred = Sigmoid(z)
    loss = Square_Loss(y_pred, y_train)

    gradient_W = np.dot((y_pred-y_train).T, x_train)/x_train.shape[0]
    gradient_B = np.mean(y_pred-y_train)

    W = W - (LR * gradient_W)
    B = B - (LR * gradient_B)

    i = i+1

    if(i%5000 == 0):
        print(f" {i} = W: {W:.6f}, B: {B:.6f}, loss: {loss:.6f}")


Result = Sigmoid(np.dot(x_test, W)+B)
Test = y_test.values


DF_Result = pd.DataFrame()
DF_Result["Test"] = Test
DF_Result["LogReg"] = Result

print("")
print(DF_Result)



# Source
# https://financial-engineering.medium.com/logistic-regression-without-sklearn-107e9ea9a9b6
