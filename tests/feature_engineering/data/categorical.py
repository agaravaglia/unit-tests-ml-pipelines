from typing import List, Dict, Any

import pandas as pd


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scenarios
    """
    if function_name == "fill_categorical_values": 
        return [
            {
                "dataframe": pd.DataFrame([[1, "2"], [2, None], [4, "5"]], columns=["a", "b"]),
                "expected_output": pd.DataFrame([[1, "2"], [2, "missing_value"], [4, "5"]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, "2"], [2, None], [None, "5"]], columns=["a", "b"]),
                "expected_output": pd.DataFrame([[1.0, "2"], [2.0, "missing_value"], ["missing_value", "5"]], columns=["a", "b"]),
            },
        ]
    elif function_name == "convert_categorical_to_onehot":
        return [
            {
                "dataframe": pd.DataFrame([["category_1"], ["category_2"]], columns=["a"]),
                "expected_output": pd.DataFrame([[1, 0], [0, 1]], columns=["a_category_1", "a_category_2"]),
            },
            {
                "dataframe": pd.DataFrame([["category_1"], ["category_2"], [None]], columns=["a"]),
                "expected_output": pd.DataFrame([[1, 0], [0, 1], [0, 0]], columns=["a_category_1", "a_category_2"]),
            },
            {
                "dataframe": pd.DataFrame([["category_1", 100], ["category_2", 1000], [None, 10000]], columns=["a", "b"]),
                "expected_output": pd.DataFrame([[100, 1, 0], [1000, 0, 1], [10000, 0, 0]], columns=["b", "a_category_1", "a_category_2"]),
            },
        ]
    elif function_name == "calculate_categorical_features":
        return [
            {
                "dataframe": pd.DataFrame([["category_1", 100], ["category_2", 1000], [None, 10000]], columns=["a", "b"]),
                "features": ["a"],
                "expected_output": pd.DataFrame([[1, 0, 0], [0, 1, 0], [0, 0, 1]], columns=["a_category_1", "a_category_2", "a_missing_value"]),
            },
            {
                "dataframe": pd.DataFrame([["category_1", 100], ["category_2", 1000], [None, 10000]], columns=["a", "b"]),
                "features": ["c"],
                "expected_output": None
            }
        ]