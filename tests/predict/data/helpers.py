import pandas as pd

from tests._pytest_utilities.features import classification_table, feature_names_default


def data(function_name):
    
    if function_name == "load_features_datasets": 
        return [
             {
                "files_to_save": {
                    "clean__features_test.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "clean__target_test.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": {
                    "features": pd.DataFrame([1, 2], columns=["a"]),
                    "target": pd.DataFrame([3, 4], columns=["b"])
                },
            },
        ]
    elif function_name == "batch_prediction": 
        return [
            {
                "model_name": "model_3_features.joblib",
                "data": classification_table(n_samples=10, n_features=3),
                "expected_output": {
                    "predictions.csv": pd.DataFrame(
                        [
                            [1], [0], [0], [0], [0], [1], [1], [0], [1], [1]
                        ],
                        columns=["is_legendary"]
                    )
                }
            },
            {
                "model_name": "model_25_features.joblib",
                "data": classification_table(n_samples=10, n_features=25),
                "expected_output": {
                    "predictions.csv": pd.DataFrame(
                        [
                            [0], [0], [1], [0], [0], [0], [0], [0], [1], [0]
                        ],
                        columns=["is_legendary"]
                    )
                }
            },
            {
                "model_name": "model_25_features.joblib",
                "data": classification_table(n_samples=10, n_features=2),
                "expected_output": None
            }
        ]