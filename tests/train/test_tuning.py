import pytest
from pytest import TempdirFactory
from typing import Dict, Any

import numpy as np

from src.utilities.data import load_sklear_model
from tests._pytest_utilities.dataframes import compare_dataframe_transformation, compare_dataframe_dictionaries
from tests._pytest_utilities.models import check_model

from tests.train.data.tuning import data
from src.train.tuning import (
    objective_function,
    tune_hyperparameters
)


@pytest.mark.parametrize(
    "scenario",
    data("objective_function")
)
def test__objective_function(
    scenario: Dict[str, Any],
    tmpdir_factory: TempdirFactory
):
    """
    Test fit_sklearn_class
    """
    output = objective_function(
        **scenario["params"]
    )
    
    # Make assertions
    assert output["loss"] == scenario["expected_output"]["loss"]
    assert output["hyperparameters"] == scenario["expected_output"]["hyperparameters"]
    assert output["status"] == scenario["expected_output"]["status"]


@pytest.mark.parametrize(
    "scenario",
    data("tune_hyperparameters")
)
def test__objective_function(
    scenario: Dict[str, Any],
):
    """
    Test tune_hyperparameters
    """
    np.random.seed(100)

    output = tune_hyperparameters(
        **scenario["params"]
    )
    
    # Make assertions
    for key in output.keys():
        print(f"\nKEY: {key}")
        assert output[key] == scenario["expected_output"][key]
