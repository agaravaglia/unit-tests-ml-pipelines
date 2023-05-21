from typing import Optional, Callable, Dict

import pandas as pd


def compare_dataframe_transformation(
    func: Callable,
    expected_output: Optional[pd.DataFrame],
    **kwargs
): 
    """
    Standard test for a function that exectues a transformation on DataFrame.
    """
    # Execute function
    output = func(**kwargs)

    # Compare output
    try:
        # If it goes through, dataframes should be equals
        pd.testing.assert_frame_equal(
            left=expected_output,
            right=output,
            check_dtype=False
        )
    except:
        # if fails, we expect nones
        assert (expected_output is None) and (output is None)


def compare_dataframe_dictionaries(
    dict_1: Dict[str, pd.DataFrame],
    dict_2: Dict[str, pd.DataFrame],
) -> bool:
    """
    Compare if two dictionary of dataframes are the same
    """
    # Check both inputs are dictionary
    assert isinstance(dict_1, Dict)
    assert isinstance(dict_2, Dict)

    # Check keys are the same
    assert set(dict_1.keys()) == set(dict_2.keys())

    # Check dataframes are the same
    for key in set(dict_1.keys()):
        try:
            pd.testing.assert_frame_equal(
                left=dict_1[key],
                right=dict_2[key],
                check_dtype=False
            )
        except:
            assert dict_1[key] is None and dict_2[key] is None
    return True