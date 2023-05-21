import shutil
import pytest
from pytest import TempdirFactory
from typing import Dict, Any

from tests._pytest_utilities.datasets import mock_loading_datasets
from tests._pytest_utilities.dataframes import compare_dataframe_transformation, compare_dataframe_dictionaries
from tests._pytest_utilities.models import check_model

from tests.train.data.helpers import data
from src.train.helpers import (
    load_features_datasets,
    fit_sklearn_class
)


@pytest.mark.parametrize(
    "scenario",
    data("load_features_datasets")
)
def test__load_features_datasets(
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
        loading_function=load_features_datasets,
        **scenario
    )

    # Remove directory
    shutil.rmtree(str(mock_data_directory))


@pytest.mark.parametrize(
    "scenario",
    data("fit_sklearn_class")
)
def test__fit_sklearn_class(
    scenario: Dict[str, Any],
    tmpdir_factory: TempdirFactory
):
    """
    Test fit_sklearn_class
    """
    check_model(
        model=fit_sklearn_class(
            hyperparameters=scenario["hyperparameters"],
            X=scenario["X"],
            y=scenario["y"]
        ),
        expected_model=scenario["expected_model"]
    )