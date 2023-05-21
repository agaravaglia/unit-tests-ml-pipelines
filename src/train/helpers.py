from pathlib import Path
from typing import Dict

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

from src.utilities.errors import error_catch
from src.utilities.data import load_dataset, save_sklear_model
from src.utilities.logging import Logger
from src.train.tuning import tune_hyperparameters


logger = Logger(module="train.helpers")


def load_features_datasets(
    dataset_folder: Path
): 
    """
    Load the raw datasets from the folder
    """
    return {
        "features":load_dataset(dataset_folder / "clean__features_train.csv"),
        "target": load_dataset(dataset_folder / "clean__target_train.csv")
    }


@error_catch
def train_model(
    data: Dict[str, pd.DataFrame]
):
    """
    Tune hyperparameters and train best combination
    """
    # select hyperparameters
    logger.info(msg="Start tuning")
    hyperparameters = tune_hyperparameters(X=data["features"], y=data["target"])
    logger.info(msg="End tuning")

    # Train model
    return fit_sklearn_class(hyperparameters, data["features"], data["target"])


@error_catch
def fit_sklearn_class(
    hyperparameters: Dict[str, any],
    X: pd.DataFrame,
    y: pd.DataFrame 
) -> LogisticRegression:
    """
    Train model for given hyperparameters and data
    """
    logger.info(msg="Start training")
    np.random.seed(100)

    # initialize model
    classifier = LogisticRegression(**hyperparameters)

    # Train
    classifier.fit(X, y)
    logger.info(msg="End training")
    return classifier
