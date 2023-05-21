from typing import List, Dict, Any

import pandas as pd


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scenarios
    """
    if function_name == "load_raw_datasets": 
        return [
            {
                "files_to_save": {
                    "raw_pokemon_index.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "raw_pokemon_data.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": {
                    "raw_pokemon_index": pd.DataFrame([1, 2], columns=["a"]),
                    "raw_pokemon_data": pd.DataFrame([3, 4], columns=["b"])
                },
            },
            {
                "files_to_save": {
                    "raw_pokemon_index.csv": pd.DataFrame([1, 2], columns=["a"]),
                },
                "expected_output": {
                    "raw_pokemon_index": pd.DataFrame([1, 2], columns=["a"]),
                    "raw_pokemon_data": None
                },
            },
            {
                "files_to_save": {
                    "raw_pokemon_data.csv": pd.DataFrame([1, 2], columns=["a"]),
                },
                "expected_output": {
                    "raw_pokemon_index": None,
                    "raw_pokemon_data": pd.DataFrame([1, 2], columns=["a"]),
                },
            }
        ]
    elif function_name == "assert_data_quality":
        return [
            {
                "data": {
                    "raw_pokemon_index": pd.DataFrame([[1, 2], [3, 4]], columns=["pokedex_number", "name"]),
                    "raw_pokemon_data": pd.DataFrame([[5, 6], [7, 8]], columns=["pokedex_number", "another_column"])
                },
                "expected_output": True
            },
            {
                "data": {
                    "raw_pokemon_index": pd.DataFrame([[1, 2], [1, 4]], columns=["pokedex_number", "name"]),
                    "raw_pokemon_data": pd.DataFrame([[5, 6], [7, 8]], columns=["pokedex_number", "another_column"])
                },
                "expected_output": None
            },
            {
                "data": {
                    "raw_pokemon_index": pd.DataFrame([[1, 2], [None, 4]], columns=["pokedex_number", "name"]),
                    "raw_pokemon_data": pd.DataFrame([[5, 6], [7, 8]], columns=["pokedex_number", "another_column"])
                },
                "expected_output": None
            },
            {
                "data": {
                    "raw_pokemon_index": pd.DataFrame([[1, 2], [3, 4]], columns=["pokedex_number", "name"]),
                    "raw_pokemon_data": pd.DataFrame([[5, 6], [5, 8]], columns=["pokedex_number", "another_column"])
                },
                "expected_output": None
            },
            {
                "data": {
                    "raw_pokemon_index": pd.DataFrame([[1, 2], [3, 4]], columns=["pokedex_number", "name"]),
                    "raw_pokemon_data": pd.DataFrame([[5, 6], [5, 6]], columns=["pokedex_number", "another_column"])
                },
                "expected_output": True
            }
        ]
    elif function_name == "calculate_intermediate_df":
        return [
            {
                "raw_data": {
                    "raw_pokemon_data": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "pokémon HELLO1"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 300, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "classification"]
                    ),
                    "raw_pokemon_index": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                            [200, 'Pokemon 2'],
                            [300, 'Pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    ),
                },
                "expected_output": pd.DataFrame(
                    [
                        ["pokemon 1", 100, "['ability_1']", 10001, "pokémon hello1"],
                        ["pokemon 2", 200, "['ability_2']", 20002, "hello2"],
                        ["pokemon 3", 300, "['ability_3', 'ability_4]", 30003, "hello3"],
                    ],
                    columns=["name", "pokedex_number", "abilities", "some_column", "classification"]
                )
            },
            {
                "raw_data": {
                    "raw_pokemon_data": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "pokémon HELLO1"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 300, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "classification"]
                    ),
                    "raw_pokemon_index": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                        ],
                        columns=["pokedex_number", "name"]
                    ),
                },
                "expected_output": pd.DataFrame(
                    [
                        ["pokemon 1", 100, "['ability_1']", 10001, "pokémon hello1"],
                    ],
                    columns=["name", "pokedex_number", "abilities", "some_column", "classification"]
                )
            },
            {
                "raw_data": {
                    "raw_pokemon_data": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "pokémon HELLO1"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 300, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "NO_COLUMN"]
                    ),
                    "raw_pokemon_index": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                            [200, 'Pokemon 2'],
                            [300, 'Pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    ),
                },
                "expected_output": None
            }
        ]
    elif function_name == "calculate_staging_dfs":
        return [
            {
                "intermediate": pd.DataFrame(
                    [
                        ["pokemon 1", 100, "['ability_1']", 10001, "pokémon hello1"],
                        ["pokemon 2", 200, "['ability_2']", 20002, "hello2"],
                        ["pokemon 3", 300, "['ability_3', 'ability_4]", 30003, "hello3"],
                    ],
                    columns=["name", "pokedex_number", "abilities", "some_column", "classification"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [100, 'Pokemon 1'],
                        [200, 'Pokemon 2'],
                        [300, 'Pokemon 3'],
                    ],
                    columns=["pokedex_number", "name"]
                ),
                "expected_output": {
                    "stg__abilities.csv": pd.DataFrame(
                        [
                            [100, "ability_1"],
                            [200, "ability_2"],
                            [300, "ability_3"],
                            [300, "ability_4"],
                        ],
                        columns=["pokedex_number", "abilities"]
                    ),
                    "stg__pokemon_data.csv": pd.DataFrame(
                        [
                            ["pokemon 1", 100, 10001, "pokémon hello1"],
                            ["pokemon 2", 200, 20002, "hello2"],
                            ["pokemon 3", 300, 30003, "hello3"],
                        ],
                        columns=["name", "pokedex_number", "some_column", "classification"]
                    ),
                    "stg__pokedex.csv": pd.DataFrame(
                        [
                            [100, 'pokemon 1'],
                            [200, 'pokemon 2'],
                            [300, 'pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                }
            },
            {
                "intermediate": pd.DataFrame(
                    [
                        ["pokemon 1", 100, "['ability_1']", 10001, "pokémon hello1"],
                    ],
                    columns=["name", "pokedex_number", "ERROR", "some_column", "classification"]
                ),
                "pokedex": pd.DataFrame(
                    [
                        [100, 'Pokemon 1'],
                        [200, 'Pokemon 2'],
                        [300, 'Pokemon 3'],
                    ],
                    columns=["pokedex_number", "name"]
                ),
                "expected_output": {
                    "stg__abilities.csv": None,
                    "stg__pokemon_data.csv": None,
                    "stg__pokedex.csv": pd.DataFrame(
                        [
                            [100, 'pokemon 1'],
                            [200, 'pokemon 2'],
                            [300, 'pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                },
            },
        ]
    