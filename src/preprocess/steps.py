from typing import List

import pandas as pd
import numpy as np

from src.utilities.errors import error_catch

@error_catch
def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Drop the duplicates of the dataframe
    """
    return dataframe.drop_duplicates()


@error_catch
def identify_string_columns(dataframe: pd.DataFrame) -> List[str]:
    """
    Identify the list of columns that are not numerical
    """
    return dataframe.select_dtypes(exclude=[np.number]).columns.tolist()


@error_catch
def lower_case(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all string columns to lower case
    """
    for col in identify_string_columns(dataframe=dataframe):
        dataframe.loc[:, col] = dataframe.loc[:, col].str.lower()
    return dataframe


@error_catch
def drop_japanese_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove japanese name to avoid issues
    """
    return (
        dataframe
        .drop("japanese_name", axis=1)
    )


@error_catch
def clean_classification(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the suffix 'pkèmon' from column values
    """
    return (
        dataframe
        .assign(
            classification=lambda df: df.classification.str.replace(" pokémon", "")
        )
    )

@error_catch
def filter_by_valid_pokedex_number(
    dataframe: pd.DataFrame,
    pokedex: pd.DataFrame
) -> pd.DataFrame:
    """
    Inner join with pokedex number to identify valid pokemons
    """
    return (
        dataframe
        .merge(
            pokedex[["pokedex_number"]],
            on="pokedex_number",
            how="inner",
            validate="one_to_one"
        )
    )


@error_catch
def extract_abilities_lookup(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Create dataframe of abilities lookup
    """
    return (
        dataframe[["pokedex_number", "abilities"]]
        [lambda df: ~df.abilities.isnull() & (df.abilities != "")]
        .assign(
            abilities=lambda df: df.abilities.str.replace("\'|\[|\]", "", regex=True).str.split(", ")
        )
        .explode("abilities")
        [["pokedex_number", "abilities"]] 
        .drop_duplicates()
        .reset_index(drop=True)
    )


@error_catch
def drop_abilities(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Drop the abilities dataframe
    """
    return dataframe.drop("abilities", axis=1)