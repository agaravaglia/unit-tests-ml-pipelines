from typing import List, Dict, Any

import pandas as pd


def data(function_name : str) -> List[Dict[str, Any]]:
    """
    Create data for testing scnearios
    """
    if function_name == "main":
        return [
            {
                "files_to_save": {},
                "create_subfolders": True,
                "expected_output": "OUTPUT: Loading failed.",
                "expected_datasets": {}
            },
            {
                "files_to_save": {
                    "raw/raw_pokemon_data.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "raw/raw_pokemon_index.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "create_subfolders": True,
                "expected_output":"OUTPUT: Data quality check failed.",
                "expected_datasets": {}
            },
            {
                "create_subfolders": True,
                "files_to_save": {
                    "raw/raw_pokemon_data.csv": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "pokémon HELLO1"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 200, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "classification"]
                    ),
                    "raw/raw_pokemon_index.csv": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                            [200, 'Pokemon 2'],
                            [300, 'Pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                },
                "expected_output":"OUTPUT: Data quality check failed.",
                "expected_datasets": {}
            },
            {
                "create_subfolders": False,
                "files_to_save": {
                    "raw/raw_pokemon_data.csv": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "pokémon HELLO1"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 300, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "classification"]
                    ),
                    "raw/raw_pokemon_index.csv": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                            [200, 'Pokemon 2'],
                            [300, 'Pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                },
                "expected_output": "OUTPUT: Error in saving staging csvs.",
                "expected_datasets": {},
            },
            {
                "create_subfolders": True,
                "files_to_save": {
                    "raw/raw_pokemon_data.csv": pd.DataFrame(
                        [
                            ["Pokemon 1", 100, "['ability_1']", "japanese_name_1", 10001, "HELLO1 pokémon"],
                            ["Pokemon 2", 200, "['ability_2']", "japanese_name_2", 20002, "HELLO2"],
                            ["Pokemon 3", 300, "['ability_3', 'ability_4]", "japanese_name_3", 30003, "HELLO3"],
                            ["Pokemon 4", 400, None, "japanese_name_4", 40004, "HELLO4"],
                        ],
                        columns=["name", "pokedex_number", "abilities", "japanese_name", "some_column", "classification"]
                    ),
                    "raw/raw_pokemon_index.csv": pd.DataFrame(
                        [
                            [100, 'Pokemon 1'],
                            [200, 'Pokemon 2'],
                            [300, 'Pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                },
                "expected_output": "OUTPUT: Preprocess complete.",
                "expected_datasets": {
                    "pipeline/stg__abilities.csv": pd.DataFrame(
                        [
                            [100, "ability_1"],
                            [200, "ability_2"],
                            [300, "ability_3"],
                            [300, "ability_4"],
                        ],
                        columns=["pokedex_number", "abilities"]
                    ),
                    "pipeline/stg__pokemon_data.csv": pd.DataFrame(
                        [
                            ["pokemon 1", 100, 10001, "hello1"],
                            ["pokemon 2", 200, 20002, "hello2"],
                            ["pokemon 3", 300, 30003, "hello3"],
                        ],
                        columns=["name", "pokedex_number", "some_column", "classification"]
                    ),
                    "pipeline/stg__pokedex.csv": pd.DataFrame(
                        [
                            [100, 'pokemon 1'],
                            [200, 'pokemon 2'],
                            [300, 'pokemon 3'],
                        ],
                        columns=["pokedex_number", "name"]
                    )
                }
            }
        ] 