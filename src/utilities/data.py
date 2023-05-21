import os
import pickle
from pathlib import Path
from typing import Dict

import pandas as pd
from sklearn.linear_model import LogisticRegression

from src.utilities.errors import error_catch


@error_catch
def get_datset_dir():
    """
    Initialize dataset directory
    """
    return (Path().cwd() / "data" / "datasets")


@error_catch
def get_model_dir():
    """
    Initialize dataset directory
    """
    return (Path().cwd() / "data" / "models")


@error_catch
def load_dataset(
    file: Path
) -> pd.DataFrame:
    """
    Function that loads a file from a path
    """
    return pd.read_csv(file, sep=";")


@error_catch
def save_dataset(
    dataframe: pd.DataFrame,
    path: Path
) -> bool:
    """
    Save Dataframe as CSV into file.
    """
    dataframe.to_csv(path, sep=";", index=False)
    return True


def save_dataframes_dict(
    dfs: Dict[str, pd.DataFrame],
    dataset_dir: Path
) -> bool:
    results = [
        save_dataset(dataframe=df, path=dataset_dir / file_name)
        for file_name, df in dfs.items()
    ]
    return all(results)


@error_catch
def save_sklear_model(
    obj: LogisticRegression,
    filename: Path
) -> bool:
    """
    Dump model as pickle
    """
    with open(str(filename), "wb") as file:
        pickle.dump(obj, file=file)
    return True


@error_catch
def load_sklear_model(
    filename: Path
) -> bool:
    """
    Dump model as pickle
    """
    with open(str(filename), "rb") as file:
        model = pickle.load(file=file)
    return model
