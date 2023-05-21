from typing import List, Dict, Any

import pandas as pd


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scenarios
    """
    if function_name == "fill_numerical_nan": 
        return [
            {
                "dataframe": pd.DataFrame([[1, 2], [None, 3], [4, 5]], columns=["a", "b"]),
                "col": "a",
                "expected_output": pd.DataFrame([[1.0, 2], [2.5, 3], [4.0, 5]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "hello"], [None, "world"], [4, "!"]], columns=["a", "b"]),
                "col": "a",
                "expected_output": pd.DataFrame([[1.0, "hello"], [2.5, "world"], [4.0, "!"]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "hello"], [2.5, "world"], [4, "!"]], columns=["a", "b"]),
                "col": "a",
                "expected_output": pd.DataFrame([[1.0, "hello"], [2.5, "world"], [4.0, "!"]], columns=["a", "b"]),
            }
        ]
    elif function_name == "fill_numerical_features":
        return [
            {
                "dataframe": pd.DataFrame([[1, 2, 10], [None, 3, None], [4, 5, 100]], columns=["a", "b", "c"]),
                "features": ["a", "c"],
                "expected_output": pd.DataFrame([[1.0, 2, 10.], [2.5, 3, 55.], [4.0, 5, 100.]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2, 10], [None, 3, None], [4, 5, 100]], columns=["a", "b", "c"]),
                "features": ["a", "b", "c"],
                "expected_output": pd.DataFrame([[1.0, 2, 10.], [2.5, 3, 55.], [4.0, 5, 100.]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2, 10], [None, 3, None], [4, 5, 100]], columns=["a", "b", "c"]),
                "features": ["a", "b"],
                "expected_output": pd.DataFrame([[1.0, 2, 10], [2.5, 3, None], [4.0, 5, 100]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "2", 10], [None, None, None], [4, "5", 100]], columns=["a", "b", "c"]),
                "features": ["b"],
                "expected_output": None
            },
        ]
    elif function_name == "standardize_numerical_features":
        return [
            {
                "dataframe": pd.DataFrame([[1, 15, 101], [2, 25, 202], [3, 35, 303]], columns=["a", "b", "c"]),
                "expected_output": pd.DataFrame([[-1., -1., -1.], [0., 0., 0.,], [1., 1., 1.]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 10, 100], [2, 20, 200], [3, 30, 300]], columns=["a", "b", "c"]),
                "expected_output": pd.DataFrame([[-1., -1., -1.], [0., 0., 0.,], [1., 1., 1.]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "10", 100], [2, 20, 200], [3, 30, 300]], columns=["a", "b", "c"]),
                "expected_output": None
            },
            {
                "dataframe": pd.DataFrame([[1], [2], [None], [3]], columns=["a"]),
                "expected_output": pd.DataFrame([[-1.], [0.], [None], [1.]], columns=["a"]),
            },
        ]
    elif function_name == "calculate_numerical_features":
        return [
            {
                "dataframe": pd.DataFrame([[1, 15, 101], [2, 25, 202], [3, 35, 303]], columns=["a", "b", "c"]),
                "features": ["a", "b", "c"],
                "expected_output": pd.DataFrame([[-1., -1., -1.], [0., 0., 0.,], [1., 1., 1.]], columns=["a", "b", "c"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 15, 101], [2, 25, 202], [3, 35, 303]], columns=["a", "b", "c"]),
                "features": ["a", "b"],
                "expected_output": pd.DataFrame([[-1., -1.], [0., 0.,], [1., 1.]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 15, 101], [None, 25, 202], [3, 35, 303]], columns=["a", "b", "c"]),
                "features": ["a", "b"],
                "expected_output": pd.DataFrame([[-1., -1.], [0., 0.,], [1., 1.]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "15", 101], [None, 25, 202], [3, 35, 303]], columns=["a", "b", "c"]),
                "features": ["a", "b"],
                "expected_output": None
            }
        ]