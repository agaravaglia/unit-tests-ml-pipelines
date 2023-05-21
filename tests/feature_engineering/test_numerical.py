import pytest
from typing import Dict, Any

from tests._pytest_utilities.dataframes import compare_dataframe_transformation
from tests.feature_engineering.data.numerical import data
from src.feature_engineering.numerical import (
    fill_numerical_nan,
    fill_numerical_features,
    standardize_numerical_features,
    calculate_numerical_features
)


@pytest.mark.parametrize(
    "scenario",
    data("fill_numerical_nan")
)
def test__fill_numerical_nan(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=fill_numerical_nan,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("fill_numerical_features")
)
def test__fill_numerical_features(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=fill_numerical_features,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("standardize_numerical_features")
)
def test__standardize_numerical_features(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=standardize_numerical_features,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("calculate_numerical_features")
)
def test__calculate_numerical_features(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=calculate_numerical_features,
        **scenario
    )