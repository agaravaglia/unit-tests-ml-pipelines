import pandas as pd
import numpy as np


from hyperopt import STATUS_OK

from tests._pytest_utilities.features import classification_table


def data(function_name):
    
    if function_name == "objective_function": 
        return [
            {
                "params": {
                    "hyperparameters": {},
                    "X": classification_table(n_samples=10, n_features=3)["features"],
                    "y": classification_table(n_samples=10, n_features=3)["target"],
                },
                "expected_output": {
                    "loss": -np.mean([1., 1., 1., 1., 0.6666666666666666]),
                    "hyperparameters": {},
                    'status': STATUS_OK
                }
            },
            {
                "params": {
                    "hyperparameters": {},
                    "X": classification_table(n_samples=30, n_features=3)["features"],
                    "y": classification_table(n_samples=10, n_features=3)["target"],
                },
                "expected_output": {
                    "loss": -np.mean([-1]),
                    "hyperparameters": {},
                    'status': STATUS_OK
                }
            }
        ]
    elif function_name == "tune_hyperparameters":
        return [
            {
                "params": {
                    "X": classification_table(n_samples=10, n_features=3)["features"],
                    "y": classification_table(n_samples=10, n_features=3)["target"],
                },
                "expected_output": {'class_weight': None, 'fit_intercept': True, 'max_iter': 1500, 'penalty': 'l1', 'solver': 'liblinear'}
            },
            {
                "params": {
                    "X": classification_table(n_samples=100, n_features=10)["features"],
                    "y": classification_table(n_samples=100, n_features=10)["target"],
                },
                "expected_output": {'class_weight': 'balanced', 'fit_intercept': False, 'max_iter': 1000, 'penalty': 'l2', 'solver': 'saga'}
            },
            {
                "params": {
                    "X": classification_table(n_samples=50, n_features=10)["features"],
                    "y": classification_table(n_samples=100, n_features=10)["target"],
                },
                "expected_output": {'class_weight': 'balanced', 'fit_intercept': True, 'max_iter': 600, 'penalty': 'l2', 'solver': 'liblinear'}
            },
        ]