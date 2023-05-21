from typing import List, Dict, Any

import pandas as pd

from tests._pytest_utilities.features import feature_names_default, classification_table


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scnearios
    """
    if function_name == "main":
        return [
            {
                "files_to_save": {},
                "expected_output": "OUTPUT: Loading failed.",
                "expected_model": None
            },
            {
                "files_to_save": {
                    "pipeline/clean__features_train.csv": classification_table(100, 5)["features"],
                    "pipeline/clean__target_train.csv": classification_table(100, 5)["target"]
                },
                "expected_output": "OUTPUT: Training complete.",
                "expected_model": {
                    "feature_names_in_": feature_names_default(5),
                    "n_features_in_": 5
                }
            },
        ] 