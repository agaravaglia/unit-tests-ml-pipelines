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
                "expected_output": "OUTPUT: Loading failed.",
                "expected_datasets": {}
            },
            {
                "files_to_save": {
                    "pipeline/stg__pokemon_data.csv": pd.DataFrame([1, 2], columns=["a"]),
                    "pipeline/stg__pokedex.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": "OUTPUT: Failed computing features.",
                "expected_datasets": {}
            },
            {
                "files_to_save": {
                    "pipeline/stg__pokemon_data.csv": pd.DataFrame(
                        [
                            [100, "pokemon_1", 100, 1000, 1, 1, 1, 1, 1, 1, 1, 1, 1, "water", "poison", 1],
                            [200, "pokemon_2", 200, 2000, 2, 2, 2, 2, 2, 2, 2, 2, 2, "fire", None, 1],
                            [300, "pokemon_3", 300, 3000, 3, 3, 3, 3, 3, 3, 3, 3, 3, "grass", "poison", 0],
                            [400, "pokemon_4", 400, 4000, 4, 4, 4, 4, 4, 4, 4, 4, 4, "dragon", "water", 0],
                            [500, "pokemon_5", 500, 5000, 5, 5, 5, 5, 5, 5, 5, 5, 5, "water", None, 0],
                        ],
                        columns=[
                            "pokedex_number",
                            "name",
                            'hp',
                            'experience_growth',
                            'attack',
                            'base_total',
                            'defense',
                            'generation',
                            'speed',
                            'sp_defense',
                            'sp_attack',
                            'height_m',
                            'weight_kg',
                            "type1",
                            "type2",
                            "is_legendary"
                        ]
                    ),
                    "pipeline/stg__pokedex.csv": pd.DataFrame([3, 4], columns=["b"])
                },
                "expected_output": "OUTPUT: Feature engineering complete.",
                "expected_datasets":  {
                    "pipeline/clean__features_train.csv": pd.DataFrame(
                        [
                            [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000,   0.000000, 0, 0, 1, 0, 0, 1, 0],
                            [0.632456, 0.632456, 0.632456, 0.632456, 0.632456, 0.632456, 0.632456, 0.632456, 0.632456, 0.632456,   0.632456, 1, 0, 0, 0, 0, 0, 1],
                            [1.264911, 1.264911, 1.264911, 1.264911, 1.264911, 1.264911, 1.264911, 1.264911, 1.264911, 1.264911,   1.264911,  0, 0, 0, 1, 1, 0, 0],
                            [-1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911, -1.264911,  0, 0, 0, 1, 0, 1, 0],
                            #[-0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, 0, 0, 0, 1, 0, 0],
                        ],
                        columns=[
                            'hp',
                            'experience_growth',
                            'attack',
                            'base_total',
                            'defense',
                            'generation',
                            'speed',
                            'sp_defense',
                            'sp_attack',
                            'height_m',
                            'weight_kg',
                            "type1_dragon",
                            "type1_fire",
                            "type1_grass",
                            "type1_water",
                            "type2_missing_value",
                            "type2_poison",
                            "type2_water"
                        ],
                    ),
                    "pipeline/clean__target_train.csv": pd.DataFrame([[0], [0], [0], [1]], columns=["is_legendary"]),
                    "pipeline/clean__features_test.csv": pd.DataFrame(
                        [
                            [-0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, -0.632456, 0, 1, 0, 0, 1, 0, 0],
                        ],
                        columns=[
                            'hp',
                            'experience_growth',
                            'attack',
                            'base_total',
                            'defense',
                            'generation',
                            'speed',
                            'sp_defense',
                            'sp_attack',
                            'height_m',
                            'weight_kg',
                            "type1_dragon",
                            "type1_fire",
                            "type1_grass",
                            "type1_water",
                            "type2_missing_value",
                            "type2_poison",
                            "type2_water"
                        ],
                    ),
                    "pipeline/clean__target_test.csv": pd.DataFrame([[1]], columns=["is_legendary"]),
                }
            }
        ]