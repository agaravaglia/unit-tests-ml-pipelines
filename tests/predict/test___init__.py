from typing import Dict, Any
import pytest
from pathlib import Path
from pytest import TempdirFactory

from src.predict import main
from src.utilities.data import save_dataframes_dict, load_sklear_model
from tests.predict.data import data
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
    test_model_directory = Path().cwd() / "data/test-models"

    # Setup files in directory
    save_dataframes_dict(
        dfs=scenario["files_to_save"],
        dataset_dir=mock_data_directory
    )

    # Execute function
    output = main(
        dataset_dir=mock_data_directory,
        model_dir=test_model_directory
    )

     # Check output is as expected
    assert output == scenario["expected_output"]

    try:
        check_saved_datasets(
            mock_data_directory=mock_data_directory,
            expected_output=scenario["expected_datasets"]
        )
    except:
        assert scenario["expected_datasets"] is None
