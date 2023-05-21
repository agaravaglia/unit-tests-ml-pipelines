from typing import List

import numpy as np
import pandas as pd

from src.utilities.errors import error_catch

CATEGORICAL_FEATURES = [
    "type1",
    "type2"
]


@error_catch
def fill_categorical_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    For now, missing values are filled with 'missing_value'
    """
    return (
        dataframe.fillna("missing_value")
    )
    

@error_catch
def convert_categorical_to_onehot(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the column into a pivot table for onehot
    """
    return (
        pd.get_dummies(dataframe).astype("int")
    )
    
    
@error_catch
def calculate_categorical_features(
    dataframe: pd.DataFrame,
    features: List[str] = CATEGORICAL_FEATURES  
) -> pd.DataFrame:
    """
    Calculate categorical features
    """
    return (
        dataframe[features]
        .pipe(fill_categorical_values)
        .pipe(convert_categorical_to_onehot)
    )
