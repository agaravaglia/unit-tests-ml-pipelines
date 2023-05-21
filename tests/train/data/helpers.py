import pandas as pd

from tests._pytest_utilities.features import classification_table, feature_names_default


def data(function_name):
    
    if function_name == "load_features_datasets": 
        return [
             {
                "files_to_save": {
                    "clean__features_train.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "clean__target_train.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": {
                    "features": pd.DataFrame([1, 2], columns=["a"]),
                    "target": pd.DataFrame([3, 4], columns=["b"])
                },
            },
        ]
    elif function_name == "fit_sklearn_class":
        return [
            {
                "hyperparameters": {},
                "X": classification_table(n_samples=10, n_features=3)["features"],
                "y": classification_table(n_samples=10, n_features=3)["target"],
                "expected_model": {
                    "feature_names_in_": feature_names_default(3),
                    "n_features_in_": 3
                }
            },
            {
                "hyperparameters": {},
                "X": classification_table(n_samples=100, n_features=25)["features"],
                "y": classification_table(n_samples=100, n_features=25)["target"],
                "expected_model": {
                    "feature_names_in_": feature_names_default(25),
                    "n_features_in_": 25
                }
            },
            {
                "hyperparameters": {},
                "X": classification_table(n_samples=1000, n_features=30)["features"],
                "y": classification_table(n_samples=1000, n_features=30)["target"],
                "expected_model": {
                    "feature_names_in_": feature_names_default(30),
                    "n_features_in_": 30
                }
            },
            {
                "hyperparameters": {},
                "X": classification_table(n_samples=100, n_features=7)["features"],
                "y": classification_table(n_samples=100, n_features=7)["target"],
                "expected_model": {
                    "feature_names_in_": feature_names_default(7),
                    "n_features_in_": 7
                }
            },
            {
                "hyperparameters": {},
                "X": None,
                "y": classification_table(n_samples=100, n_features=25)["target"],
                "expected_model": None
            },
            {
                "hyperparameters": {},
                "X": classification_table(n_samples=20, n_features=2)["features"],
                "y": classification_table(n_samples=100, n_features=25)["target"],
                "expected_model": None
            },
        ]
