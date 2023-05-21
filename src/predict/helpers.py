from pathlib import Path
from typing import Dict

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

from src.utilities.data import load_dataset
from src.utilities.errors import error_catch
from src.utilities.logging import Logger


logger = Logger(module="train.helpers")


def load_features_datasets(
    dataset_folder: Path
): 
    """
    Load the raw datasets from the folder
    """
    print(dataset_folder / "clean__features_test.csv")
    return {
        "features": load_dataset(dataset_folder / "clean__features_test.csv"),
        "target": load_dataset(dataset_folder / "clean__target_test.csv")
    }


@error_catch
def batch_prediction(
    classifier: LogisticRegression,
    data: Dict[str, pd.DataFrame]
):
    """
    Make batch prediction 
    """
    # calculate predictions
    return {"predictions.csv": pd.DataFrame(classifier.predict(data["features"]), columns=["is_legendary"])}
