import pytest
import shutil
from typing import Dict, Any

import pandas as pd
from pytest import TempdirFactory

from src.preprocess.helpers import (
    load_raw_datasets,
    assert_data_quality,
    calculate_intermediate_df,
    calculate_staging_dfs
)
from tests._pytest_utilities.datasets import mock_loading_datasets
from tests ._pytest_utilities.dataframes import compare_dataframe_transformation, compare_dataframe_dictionaries
from tests.preprocess.data.helpers import data


@pytest.mark.parametrize(
    "scenario",
    data("load_raw_datasets")
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
        loading_function=load_raw_datasets,
        **scenario
    )

    # Remove directory
    shutil.rmtree(str(mock_data_directory))


@pytest.mark.parametrize(
    "scenario",
    data("assert_data_quality")
)
def test__assert_data_quality(
    scenario: Dict[str, Any],
):
    """
    Tests for assert_data_quality
    """
    assert (
        scenario["expected_output"]
        == assert_data_quality(scenario["data"])
    )


@pytest.mark.parametrize(
    "scenario",
    data("calculate_intermediate_df")
)
def test__calculate_intermediate_df(
    scenario: Dict[str, Any],
):
    """
    Tests for assert_data_quality
    """
    compare_dataframe_transformation(
        func=calculate_intermediate_df,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("calculate_staging_dfs")
)
def test__calculate_staging_dfs(
    scenario: Dict[str, Any],
):
    """
    Tests for assert_data_quality
    """
    output = calculate_staging_dfs(
        intermediate=scenario["intermediate"],
        pokedex=scenario["pokedex"],
    )

    compare_dataframe_dictionaries(
        dict_1=scenario["expected_output"],
        dict_2=output
    )
