from pathlib import Path
from typing import Dict

import pandas as pd

from src.utilities.data import load_dataset
from src.utilities.errors import error_catch
from src.preprocess.steps import *


def load_raw_datasets(
    dataset_folder: Path
): 
    """
    Load the raw datasets from the folder
    """
    return {
        "raw_pokemon_index": load_dataset(dataset_folder / "raw_pokemon_index.csv"),
        "raw_pokemon_data": load_dataset(dataset_folder / "raw_pokemon_data.csv")
    }


@error_catch
def assert_data_quality(
    data: Dict[str, pd.DataFrame]
) -> bool: 
    """
    Make sure of data quality in pokemon index
    """
    # Quality on pokemon index
    assert (
        data["raw_pokemon_index"].pokedex_number.is_unique and
        not data["raw_pokemon_index"].pokedex_number.isnull().any() and
        data["raw_pokemon_index"].name.is_unique and
        not data["raw_pokemon_index"].name.isnull().any()
    )
    # quality on pokemon data
    assert data["raw_pokemon_data"].drop_duplicates().pokedex_number.is_unique  
    # if here, all checks have worked
    return True


@error_catch
def calculate_intermediate_df(
    raw_data: Dict[str, pd.DataFrame]
) -> pd.DataFrame:
    """
    Claculate intermediate transformation
    """
    return (
        raw_data["raw_pokemon_data"]
        .pipe(remove_duplicates)
        .pipe(lower_case)
        .pipe(clean_classification)
        .pipe(drop_japanese_names)
        .pipe(
            filter_by_valid_pokedex_number,
            pokedex=raw_data["raw_pokemon_index"]
        )
    )


def calculate_staging_dfs(
    intermediate: pd.DataFrame,
    pokedex: pd.DataFrame
) -> Dict[str, pd.DataFrame]:
    """
    From the intermediate trasnformation, calculate the staging Dataframes
    """
    return {
        "stg__abilities.csv": extract_abilities_lookup(intermediate),
        "stg__pokemon_data.csv": drop_abilities(intermediate),
        "stg__pokedex.csv": lower_case(pokedex)
    }