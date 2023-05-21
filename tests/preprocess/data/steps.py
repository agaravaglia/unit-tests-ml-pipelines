from typing import List, Dict, Any

import pandas as pd


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scnearios
    """
    if function_name == "remove_duplicates": 
        return [
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4], [1, 2]], columns=["a", "b"]),
                "expected_output":  pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]),
                "expected_output":  pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]),
            }
        ]
    elif function_name == "identify_string_columns":
        return [
            {
                "dataframe": pd.DataFrame([["1", 2], ["3", 4], ["1", 2]], columns=["a", "b"]),
                "expected_output": ["a"]
            },
            {
                "dataframe": pd.DataFrame([[1, "2"], [3, "4"], [3, "2"]], columns=["a", "b"]),
                "expected_output": ["b"]
            },
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4], [3, 2]], columns=["a", "b"]),
                "expected_output": []
            },
            {
                "dataframe": pd.DataFrame([["1", "2"], ["3", "4"], ["3", "2"]], columns=["a", "b"]),
                "expected_output": ["a", "b"]
            },
            {
                "dataframe": pd.DataFrame([]),
                "expected_output": []
            }
        ]
    elif function_name == "lower_case":
        return [
            {
                "dataframe": pd.DataFrame([["Hello"], ["World"]], columns=["a"]),
                "expected_output": pd.DataFrame([["hello"], ["world"]], columns=["a"]),
            },
            {
                "dataframe": pd.DataFrame([["Hello", 100], ["World", 200]], columns=["a", "b"]),
                "expected_output": pd.DataFrame([["hello", 100], ["world", 200]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4], [3, 2]], columns=["a", "b"]),
                "expected_output": pd.DataFrame([[1, 2], [3, 4], [3, 2]], columns=["a", "b"]),
            }
        ]
    elif function_name == "drop_japanese_names":
        return [
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4], [3, 2]], columns=["a", "japanese_name"]),
                "expected_output": pd.DataFrame([[1], [3], [3]], columns=["a"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2], [3, 4], [3, 2]], columns=["a", "b"]),
                "expected_output": None
            },
        ]
    elif function_name == "clean_classification":
        return [
            {
                "dataframe": pd.DataFrame([["Hello pokémon", "ciao"], ["World", "mondo"]], columns=["classification", "other_column"]),
                "expected_output": pd.DataFrame([["Hello", "ciao"], ["World", "mondo"]], columns=["classification",  "other_column"]),
            },
            {
                "dataframe": pd.DataFrame([["pokèmon Hello"], ["World"]], columns=["classification"]),
                "expected_output": pd.DataFrame([["pokèmon Hello"], ["World"]], columns=["classification"]),
            },
            {
                "dataframe": pd.DataFrame([["Hello pokémon"], ["World"]], columns=["not_classification"]),
                "expected_output": None
            }
        ]
    elif function_name == "filter_by_valid_pokedex_number":
        return [
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                        [300, "pokèmon_3", "info_3"],
                        [400, "pokèmon_4", "info_4"]
                    ], 
                    columns=["pokedex_number", "name", "info"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [100, "pokèmon_1"],
                        [200, "pokèmon_2"],
                        [300, "pokèmon_3"],
                    ],
                    columns=["pokedex_number", "name"]
                ),
                "expected_output": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                        [300, "pokèmon_3", "info_3"],
                    ], 
                    columns=["pokedex_number", "name", "info"]
                )
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                        [300, "pokèmon_3", "info_3"],
                        [400, "pokèmon_4", "info_4"]
                    ], 
                    columns=["pokedex_number", "name", "info"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "uselsess_column"],
                        [200, "pokèmon_2", "uselsess_column"],
                        [300, "pokèmon_3", "uselsess_column"],
                    ],
                    columns=["pokedex_number", "name", "uselsess_column"]
                ),
                "expected_output": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                        [300, "pokèmon_3", "info_3"],
                    ], 
                    columns=["pokedex_number", "name", "info"]
                )
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                    ], 
                    columns=["pokedex_number", "name", "info"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [100, "pokèmon_1"],
                        [200, "pokèmon_2"],
                        [200, "pokèmon_3"],
                    ],
                    columns=["pokedex_number", "name"]
                ),
                "expected_output": None
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, "pokèmon_1", "info_1"],
                        [200, "pokèmon_2", "info_2"],
                    ], 
                    columns=["pokedex_number", "name", "info"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [1000, "pokèmon_1"],
                        [2000, "pokèmon_2"],
                    ],
                    columns=["pokedex_number", "name"]
                ),
                "expected_output": pd.DataFrame(columns=["pokedex_number", "name", "info"])
            }
        ]
    elif function_name == "extract_abilities_lookup":
        return [
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, ""],
                        [200, "some_weird string"],
                        [300, "['ability_1', 'ability_2']"],
                        [400, "['ability_3']"],
                    ],
                    columns=["pokedex_number", "abilities"]
                ),
                "expected_output": pd.DataFrame(
                    [
                        [200, "some_weird string"],
                        [300, "ability_1"],
                        [300, "ability_2"],
                        [400, "ability_3"],
                    ],
                    columns=["pokedex_number", "abilities"]
                )
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, ""],
                        [200, "some_weird string"],
                        [300, "['ability_1', 'ability_2']"],
                        [400, "['ability_3']"],
                        [300, "['ability_4', 'ability_5']"],
                        [500, None],
                    ],
                    columns=["pokedex_number", "abilities"]
                ),
                "expected_output": pd.DataFrame(
                    [
                        [200, "some_weird string"],
                        [300, "ability_1"],
                        [300, "ability_2"],
                        [400, "ability_3"],
                        [300, "ability_4"],
                        [300, "ability_5"],
                    ],
                    columns=["pokedex_number", "abilities"]
                )
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [100, ""],
                        [200, "some_weird string"],
                        [300, "['ability_1', 'ability_2']"],
                        [400, "['ability_3']"],
                        [300, "['ability_4', 'ability_5']"],
                        [500, None],
                    ],
                    columns=["pokedex_number", "another_column"]
                ),
                "expected_output": None
            },
            {
                "dataframe": pd.DataFrame(
                    [
                        [300, "['ability_1', 'ability_2']", "hello there"],
                    ],
                    columns=["pokedex_number", "abilities", "col_to_ignore"]
                ),
                "expected_output": pd.DataFrame(
                    [
                        [300, "ability_1"],
                        [300, "ability_2"],
                    ],
                    columns=["pokedex_number", "abilities"]
                )
            },
        ]
    elif function_name == "drop_abilities":
        return [
            {
                "dataframe": pd.DataFrame([[1, 2, 3]], columns=["a", "b", "abilities"]),
                "expected_output": pd.DataFrame([[1, 2]], columns=["a", "b"]),
            },
            {
                "dataframe": pd.DataFrame([[1, 2, 3]], columns=["a", "b", "c"]),
                "expected_output": None
            }
        ]