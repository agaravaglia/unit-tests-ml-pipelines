import pytest
from typing import Dict, Any

import pandas as pd

from tests._pytest_utilities.dataframes import compare_dataframe_transformation
from tests.preprocess.data.steps import data
from src.preprocess.steps import (
    remove_duplicates,
    identify_string_columns,
    lower_case,
    clean_classification,
    filter_by_valid_pokedex_number,
    extract_abilities_lookup,
    drop_abilities
)


@pytest.mark.parametrize(
    "scenario",
    data("remove_duplicates")
)
def test__remove_duplicates(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    compare_dataframe_transformation(
        func=remove_duplicates,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("identify_string_columns")
)
def test__identify_string_columns(
    scenario: Dict[str, Any]
):
    """
    Test the remove_duplicates function
    """
    output = identify_string_columns(dataframe=scenario["dataframe"])

    assert output == scenario["expected_output"]



@pytest.mark.parametrize(
    "scenario",
    data("lower_case")
)
def test__lower_case(
    scenario: Dict[str, Any]
):
    """
    Test the lower_case function
    """
    compare_dataframe_transformation(
        func=lower_case,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("clean_classification")
)
def test__clean_classification(
    scenario: Dict[str, Any]
):
    """
    Test the clean_classification function
    """
    compare_dataframe_transformation(
        func=clean_classification,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("filter_by_valid_pokedex_number")
)
def test__filter_by_valid_pokedex_number(
    scenario: Dict[str, Any]
):
    """
    Test the filter_by_valid_pokedex_number function
    """
    compare_dataframe_transformation(
        func=filter_by_valid_pokedex_number,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("extract_abilities_lookup")
)
def test__extract_abilities_lookup(
    scenario: Dict[str, Any]
):
    """
    Test the extract_abilities_lookup function
    """
    compare_dataframe_transformation(
        func=extract_abilities_lookup,
        **scenario
    )


@pytest.mark.parametrize(
    "scenario",
    data("drop_abilities")
)
def test__drop_abilities(
    scenario: Dict[str, Any]
):
    """
    Test the drop_abilities function
    """
    compare_dataframe_transformation(
        func=drop_abilities,
        **scenario
    )
