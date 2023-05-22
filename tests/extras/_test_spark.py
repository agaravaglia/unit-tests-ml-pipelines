from typing import Dict, Any

import pytest
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame as SparkDataFrame


from src.utilities.errors import error_catch
from tests._pytest_utilities.dataframes import compare_dataframe_transformation


@pytest.fixture(scope="module")
def spark() -> SparkSession:
    """
    Fixture that sets a spark session
    """
    yield (
        SparkSession
        .builder
        .master("local[2]")
        .appName("spark-session-unit-tests")
        .getOrCreate()
    )


@error_catch
def filter_for_valid_category(
    dataframe: SparkDataFrame,
) -> SparkDataFrame:
    """
    Filter dataframe vof valid category
    """
    return (
        dataframe
        .where("category = 'valid'")
    )


def data(function_name: str):
    """
    get data for tests
    """
    if function_name == "filter_for_valid_category":
        return[
            {
                "dataframe": pd.DataFrame([["valid", 10], ["valid", 20], ["not_valid", 30]], columns=["category", "a"]),
                "expected_output": pd.DataFrame([["valid", 10], ["valid", 20]], columns=["category", "a"])
            },
            {
                "dataframe": pd.DataFrame([["valid", 10], ["valid", 20], ["not_valid", 30]], columns=["b", "a"]),
                "expected_output": None
            }
        ]


@pytest.mark.parametrize(
    "scenario",
    data("filter_for_valid_category")
)
def test__filter_for_valid_category(
    spark: SparkSession,
    scenario: Dict[str, Any]
):
    """
    Filter the dataframe for the valid category
    """
    # Convert inputs to spark dataframe and execute
    output = filter_for_valid_category(
        dataframe=spark.createDataFrame(scenario["dataframe"])
    )
    
    # Try to make assertion
    try:
        # If it goes through, dataframes should be equals
        pd.testing.assert_frame_equal(
            left=scenario["expected_output"],
            right=output.toPandas(),
            check_dtype=False
        )
    except:
        # if fails, we expect nones
        assert scenario["expected_output"] is None
        assert output is None
