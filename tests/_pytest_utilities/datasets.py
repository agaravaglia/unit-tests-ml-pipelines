from pathlib import Path
from typing import Dict, Callable, Optional

from src.utilities.data import save_dataframes_dict, load_dataset
from tests._pytest_utilities.dataframes import compare_dataframe_dictionaries

import pandas as pd


def mock_loading_datasets(
    mock_data_directory: Path,
    files_to_save: Dict[str, pd.DataFrame],
    loading_function: Callable,
    expected_output
): 
    """
    Execute test of loading 
    """
    # Save all dataframes into a mock folder
    save_dataframes_dict(
        dfs=files_to_save,
        dataset_dir=mock_data_directory
    )

    # Test loading function
    output = loading_function(mock_data_directory)

    # Compare the two dictionaries
    assert compare_dataframe_dictionaries(
        dict_1=output,
        dict_2=expected_output    
    )


def check_saved_datasets(
    mock_data_directory: Path,
    expected_output: Dict[str, Optional[pd.DataFrame]]
):
    """
    Check if datasets saved are as expected
    """
    # Load data
    loaded_datasets = {
        key: (
            load_dataset(mock_data_directory / key)
            if (mock_data_directory / key).exists()
            else None
        )
        for key in expected_output.keys()
    }

    # Compare the two dictionaries
    assert compare_dataframe_dictionaries(
        dict_1=loaded_datasets,
        dict_2=expected_output    
    )
