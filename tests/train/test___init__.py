from typing import Dict, Any
import pytest
from pytest import TempdirFactory

from src.train import main
from src.utilities.data import save_dataframes_dict, load_sklear_model
from tests.train.data import data
from tests._pytest_utilities.datasets import check_saved_datasets
from tests._pytest_utilities.models import check_model


@pytest.mark.parametrize(
    "scenario",
    data("main")
)
def test__main(
    scenario: Dict[str, Any],
    tmpdir_factory: TempdirFactory
):
    """
    Test the entire preprocess module
    """
    # Create directory
    mock_data_directory = tmpdir_factory.mktemp("pytest_data")
    (mock_data_directory / "pipeline").mkdir()
    (mock_data_directory / "models").mkdir()

    # Setup files in directory
    save_dataframes_dict(
        dfs=scenario["files_to_save"],
        dataset_dir=mock_data_directory
    )

    # Execute main
    output = main(
        dataset_dir=mock_data_directory,
        model_dir=(mock_data_directory / "models")
    )

    # Check output is as expected
    assert output == scenario["expected_output"]

    check_model(
        model=load_sklear_model(filename=str(mock_data_directory / "models/sklearn_classifier.joblib")),
        expected_model=scenario["expected_model"]
    )

