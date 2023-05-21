from pathlib import Path
from typing import Dict, List

import pandas as pd
from sklearn.model_selection import train_test_split

from src.utilities.errors import error_catch
from src.utilities.data import load_dataset
from src.feature_engineering.categorical import calculate_categorical_features, CATEGORICAL_FEATURES
from src.feature_engineering.numerical import calculate_numerical_features, NUMERICAL_FEATURES


def load_stg_datasets(dataset_dir: Path) -> Dict[str, pd.DataFrame]:
    """
    Load staging data from folder
    """
    return {
        "pokemon_data": load_dataset(dataset_dir / "stg__pokemon_data.csv"),
        "pokedex": load_dataset(dataset_dir / "stg__pokedex.csv")
    }


@error_catch
def calculate_features_and_target(
    stg_data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Calculate features 
    """
    # Calculate dataframes
    features = (
        calculate_numerical_features(
            dataframe=stg_data["pokemon_data"]
        )
        .join(
            calculate_categorical_features(
                dataframe=stg_data["pokemon_data"]
            )
        )
    )
    target = stg_data["pokemon_data"][["is_legendary"]]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        random_state=100,
        test_size=0.2
    )
    return {
        "clean__features_train.csv": X_train,
        "clean__target_train.csv": y_train,
        "clean__features_test.csv": X_test,
        "clean__target_test.csv": y_test,
    }
