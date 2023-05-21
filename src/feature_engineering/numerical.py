from typing import List

import numpy as np
import pandas as pd

from src.utilities.errors import error_catch


NUMERICAL_FEATURES = [
    'hp',
    'experience_growth',
    'attack',
    'base_total',
    'defense',
    'generation',
    'speed',
    'sp_defense',
    'sp_attack',
    'height_m',
    'weight_kg',
]


@error_catch
def fill_numerical_nan(dataframe: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    For a given column, fill numerical with the mean
    """
    mean = dataframe.loc[:, col].mean()
    
    dataframe.loc[:, col] = np.where(
        ~dataframe.loc[:, col].isnull(),
        dataframe.loc[:, col],
        mean
    )
    
    return dataframe


@error_catch
def fill_numerical_features(
    dataframe: pd.DataFrame, 
    features: List[str]
) -> pd.DataFrame:
    """
    Fill numerical features
    """
    for col in features:
        dataframe = fill_numerical_nan(dataframe, col)
    
    return dataframe


@error_catch
def standardize_numerical_features(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """
    stndardize according to mean and std
    """
    return (
        (dataframe-dataframe.mean())/dataframe.std()
    )


@error_catch
def calculate_numerical_features(
    dataframe: pd.DataFrame, 
    features: List[str] = NUMERICAL_FEATURES
) -> pd.DataFrame:
    """
    Calculate numerical features
    """
    return (
        dataframe
        [features]
        .pipe(fill_numerical_features, features=features)
        .pipe(standardize_numerical_features)   
    )
