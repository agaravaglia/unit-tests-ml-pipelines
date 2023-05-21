import pytest
from typing import Dict, Any

from tests._pytest_utilities.dataframes import compare_dataframe_transformation
from tests.feature_engineering.data.categorical import data
from src.feature_engineering.categorical import (
    fill_categorical_values,
    convert_categorical_to_onehot,
    calculate_categorical_features
)


@pytest.mark.parametrize(
    "scenario",
    data("fill_categorical_values")
)
def test__fill_categorical_values(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=fill_categorical_values,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("convert_categorical_to_onehot")
)
def test__convert_categorical_to_onehot(
    scenario: Dict[str, Any]
):
    """
    Test the convert_categorical_to_onehot function
    """
    compare_dataframe_transformation(
        func=convert_categorical_to_onehot,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("calculate_categorical_features")
)
def test__calculate_categorical_features(
    scenario: Dict[str, Any]
):
    """
    Test the calculate_categorical_features function
    """
    compare_dataframe_transformation(
        func=calculate_categorical_features,
        **scenario
    )
