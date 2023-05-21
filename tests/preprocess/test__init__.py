from typing import Dict, Any
import pytest
from pytest import TempdirFactory

from src.preprocess import main
from src.utilities.data import save_dataframes_dict
from tests.preprocess.data import data
from tests._pytest_utilities.datasets import check_saved_datasets


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
    (mock_data_directory / "raw").mkdir()
    if scenario["create_subfolders"]:
        (mock_data_directory / "pipeline").mkdir()

    # Setup files in directory
    save_dataframes_dict(
        dfs=scenario["files_to_save"],
        dataset_dir=mock_data_directory
    )

    # Execute main
    output = main(dataset_dir=mock_data_directory)

    # Check output is as expected
    assert output == scenario["expected_output"]

    # Load data and compare
    check_saved_datasets(
        mock_data_directory=mock_data_directory,
        expected_output=scenario["expected_datasets"]
    )
