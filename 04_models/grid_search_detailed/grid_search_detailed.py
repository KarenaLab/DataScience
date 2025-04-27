# [P516] Grid Search Detailed

# Versions
# 01 - Apr 05th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import itertools

import numpy as np
import pandas as pd
import scipy.stats as stats

import matplotlib.pyplot as plt


# Personal Libraries
from src.stratified_continuous_kfold import stratified_continuous_kfold


# ----------------------------------------------------------------------
def grid_search_detailed(hyperparams):
    """


    """
    # Hyperparameters grid
    params_names = list(hyperparams.keys())
    params_comb = list(itertools.product(*hyperparams.values()))

    for hparams in params_comb:
        model_hparams = dict()
        for key, value in zip(params_names, hparams):
            model_hparams[key] = value

        print(model_hparams)

            
    return None


"""

# Sample data
from sklearn.datasets import load_iris
data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define parameter grid
param_grid = {'n_estimators': [10, 50, 100],
              'max_depth': [None, 10, 20],
              'min_samples_split': [2, 5]}

# Generate all combinations of parameters
param_combinations = list(itertools.product(*param_grid.values()))

# Track the best results
best_score = 0
best_params = None

# Grid Search
for combination in param_combinations:
    params = dict(zip(param_grid.keys(), combination))
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    score = accuracy_score(y_test, predictions)

    print(f"Params: {params}, Accuracy: {score}")
    
    if score > best_score:
        best_score = score
        best_params = params

print("\nBest Parameters:", best_params)
print("Best Accuracy:", best_score)
"""

if(__name__ == "__main__"):
    param_grid = {'n_estimators': [10, 50, 100],
                  'max_depth': [None, 10, 20],
                  'min_samples_split': [2, 5]}

    params = grid_search_detailed(param_grid)

    
    
