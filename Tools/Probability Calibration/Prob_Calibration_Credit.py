
import numpy as np
import pandas as pd

from sklearn.calibration import calibration_curve
from sklearn.calibration import CalibratedClassifierCV

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import roc_auc_score

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Definitions/Config

Seed = 38
plt.style.use("ekc")



# Program

print("\n ****  Probability Calibration - Credit Card Clients  **** \n")

DF = pd.read_csv("Credit_Card_Clients_2005.csv", sep= ",")


# Data Information:
# https://blog.cambridgespark.com/probability-calibration-c7252ac123f
# https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients


# Attribute Information:

# This research employed a binary variable, default payment (Yes = 1,
# No = 0), as the response variable. This study reviewed the literature
# and used the following 23 variables as explanatory variables:
#
# Limit_Bal: Amount of the given credit (NT dollar): it includes both the
#            individual consumer credit and his/her family (supplementary)
#            credit;
#
# Gender: (1 = male; 2 = female);
#
# Education: (1 = graduate school; 2 = university; 3 = high school;
#             4 = others);
#
# Marriage: (1 = married; 2 = single; 3 = others);
#
# Age (years);
#
# Pay_0 ~ Pay_6: History of past payment. We tracked the past monthly
#                payment records (from April to September, 2005) as
#                follows:
#                Pay_1 = The repayment status in September, 2005;
#                Pay_2 = the repayment status in August, 2005;
#                ...
#                Pay_6 = the repayment status in April, 2005.
#
#     Important: The measurement scale for the repayment status is:
#                   -1 = pay duly;
#                    1 = payment delay for one month;
#                    2 = payment delay for two months;
#                    ...
#                    8 = payment delay for eight months
#                    9 = payment delay for nine months and above.
#
# Bill_Amtx: Amount of bill statement (NT dollar).
#            Bill_Amt1 = amount of bill statement in September, 2005;
#            Bill_Amt2 = amount of bill statement in August, 2005;
#            ...
#            Bill_Amt6 = amount of bill statement in April, 2005.
#
# Pay_Amtx: Amount of previous payment (NT dollar).
#           Pay_Amt1 = amount paid in September, 2005;
#           Pay_Amt2 = amount paid in August, 2005;
#           ...
#           Pay_Amt6 = amount paid in April, 2005.
#


# Model

Target = "DEFAULT_PMT"

Model_Features = [ "LIMIT_BAL", "AGE", "PAY_1", "PAY_2", "PAY_3", "PAY_4",
                   "PAY_5", "PAY_6", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3",
                   "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1",
                   "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5",
                   "PAY_AMT6" ]

Data_X = DF[Model_Features]
Data_Y = DF[Target]


# Train/Test Split

X_Train, X_Test, Y_Train, Y_Test = train_test_split(Data_X, Data_Y, stratify= Data_Y, random_state= Seed)


# Create a hold out dataset to train the calibrated model to prevent overfitting

X_Model_Train, X_Valid, Y_Model_Train, Y_Valid = train_test_split(X_Train, Y_Train, stratify= Y_Train, random_state= Seed)


# Random Forest

RF_clf = RandomForestClassifier(n_estimators= 100, max_depth= 6, min_samples_split= 200, random_state= Seed, class_weight= "balanced")
RF_clf.fit(X_Model_Train, Y_Model_Train)
RF_Predictions = RF_clf.predict_proba(X_Test)
RF_ROC_Score = roc_auc_score(Y_Test, RF_Predictions[:,1])

print(f" > Random Forest ROC Score = {RF_ROC_Score:.4f}")


# Probability Calibration

Probabilities = np.arange(start= 0, stop= 1.2, step= 0.2)
RF_Fraction_Positives, RF_Mean_Predicted = calibration_curve(Y_Test, RF_Predictions[:,1], n_bins= 10)

# Plotting

fig = plt.figure()

Title = "Reliability Curve"
fig.suptitle(Title, fontsize= 14)

plt.plot(Probabilities, Probabilities, linestyle= "--", color= "orange", label= "Reference (perfectly)")
plt.plot(RF_Mean_Predicted, RF_Fraction_Positives, linestyle= "-", color= "navy", label= "Random Forest Calibrated")

plt.legend(loc= "best")
plt.savefig(Title, dpi= 240)
plt.show()



# Calibration

Calib_clf = CalibratedClassifierCV(RF_clf, method= "sigmoid", cv= "prefit")
Calib_clf.fit(X_Valid, Y_Valid)
Calibrated_Predictions = Calib_clf.predict_proba(X_Test)
Calib_ROC_Score = roc_auc_score(Y_Test, Calibrated_Predictions[:,1])

print(f" > Calibrated ROC Score = {Calib_ROC_Score:.4f}")

Probabilities = np.arange(start= 0, stop= 1.2, step= 0.2)
Cal_Fraction_Positives, Cal_Mean_Predicted = calibration_curve(Y_Test, Calibrated_Predictions[:,1], n_bins= 10)


# Plotting

fig = plt.figure()

Title = "Reliability Curve Calibrated"
fig.suptitle(Title, fontsize= 14)

plt.plot(Probabilities, Probabilities, linestyle= "--", color= "orange", label= "Reference (perfectly)")
plt.plot(RF_Mean_Predicted, RF_Fraction_Positives, linestyle= "-", color= "navy", label= f"Random Forest - ROC: {RF_ROC_Score:.4f}")
plt.plot(Cal_Mean_Predicted, Cal_Fraction_Positives, linestyle= "-", color= "darkred", label= f"Calibrated Model - ROC: {Calib_ROC_Score:.4f}")

plt.legend(loc= "best")
plt.savefig(Title, dpi= 240)
plt.show()



# Closing

print(" * \n")


# Sources

# https://scikit-learn.org/stable/modules/calibration.html



