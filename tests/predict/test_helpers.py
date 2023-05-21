import shutil
import pytest
from pathlib import Path
from pytest import TempdirFactory
from typing import Dict, Any

from src.utilities.data import load_sklear_model

from tests._pytest_utilities.datasets import mock_loading_datasets
from tests._pytest_utilities.dataframes import compare_dataframe_transformation, compare_dataframe_dictionaries
from tests._pytest_utilities.models import check_model

from tests.predict.data.helpers import data
from src.predict.helpers import (
    load_features_datasets,
    batch_prediction
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
    data("batch_prediction")
)
def test__batch_prediction(
    scenario: Dict[str, Any],
    tmpdir_factory: TempdirFactory
):
    """
    Test for predicting based on models
    """
    # Get test-model directory
    test_model_dir = Path().cwd() / "data/test-models"

    # calculate output
    output = batch_prediction(
        classifier=load_sklear_model(test_model_dir / scenario["model_name"]),
        data=scenario["data"]
    )
    # Compare dictionaries
    try:
        compare_dataframe_dictionaries(
            dict_1=output,
            dict_2=scenario["expected_output"]
        )
    except:
        assert output is None
        assert scenario["expected_output"] is None
