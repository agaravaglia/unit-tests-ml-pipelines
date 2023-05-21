import shutil
import pytest
from pytest import TempdirFactory
from typing import Dict, Any

from tests._pytest_utilities.datasets import mock_loading_datasets
from tests ._pytest_utilities.dataframes import compare_dataframe_transformation, compare_dataframe_dictionaries
from tests.feature_engineering.data.helpers import data
from src.feature_engineering.helpers import (
    load_stg_datasets,
    calculate_features_and_target
)


@pytest.mark.parametrize(
    "scenario",
    data("load_stg_datasets")
)
def test__load_raw_datasets(
    scenario: Dict[str, Any],
    tmpdir_factory: TempdirFactory
):
    """
    Test the remove_duplicates function
    """
    # Create directory
    mock_data_directory = tmpdir_factory.mktemp("pytest_data")

    # Execute the test for loading
    mock_loading_datasets(
        mock_data_directory=mock_data_directory,
        loading_function=load_stg_datasets,
        **scenario
    )

    # Remove directory
    shutil.rmtree(str(mock_data_directory))


@pytest.mark.parametrize(
    "scenario",
    data("calculate_features_and_target")
)
def test__calculate_features_and_target(
    scenario: Dict[str, Any]
):
    """
    Test the calculate_features_and_target function
    """
    output = calculate_features_and_target(
        scenario["stg_data"]
    )
    try:
        compare_dataframe_dictionaries(
            dict_1=output,
            dict_2=scenario["expected_output"]
        )
    except:
        assert scenario["expected_output"] is None
        assert output is None
