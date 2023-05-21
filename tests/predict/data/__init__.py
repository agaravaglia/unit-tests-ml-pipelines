from typing import List, Dict, Any

import pandas as pd

from tests._pytest_utilities.features import classification_table


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scnearios
    """
    if function_name == "main":
        return [
            {
                "files_to_save": {},
                "expected_output": "OUTPUT: Loading data failed.",
                "expected_datasets": None
            },
            {
                "files_to_save": {
                    "pipeline/clean__features_test.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "pipeline/clean__target_test.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": "OUTPUT: Predictions failed.",
                "expected_datasets": None
            },
            {
                "files_to_save": {
                    "pipeline/clean__features_test.csv": classification_table(n_samples=10, n_features=7)["features"],
                    "pipeline/clean__target_test.csv": classification_table(n_samples=10, n_features=7)["target"],
                },
                "expected_output": "OUTPUT: Predict complete.",
                "expected_datasets": {
                    "pipeline/predictions.csv": pd.DataFrame(
                        [[0], [1], [0], [1], [0], [1], [1], [0], [0], [0]],
                        columns=["is_legendary"]
                    )
                }
            },
        ] 