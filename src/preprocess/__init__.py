from pathlib import Path
from typing import Optional
import pandas as pd

from src.utilities.logging import Logger
from src.utilities.data import get_datset_dir, save_dataframes_dict

from src.preprocess.helpers import (
    load_raw_datasets,
    assert_data_quality,
    calculate_intermediate_df,
    calculate_staging_dfs,
)

logger = Logger(module="preprocess")


def main(dataset_dir: Optional[Path] = None):
    """
    Main function of the preprocess.
    """
    logger.info(msg="Start executing preprocess module.")
    
    # Initialize dataset directory
    if not dataset_dir:
        logger.info(msg="Get Directory.")
        dataset_dir = get_datset_dir()
    if not dataset_dir:
        logger.warning(msg="No dataset directory.")
        return "OUTPUT: No dataset directory."
    
    # Load data
    logger.info(msg="Load data.")
    raw_data = load_raw_datasets(dataset_folder=dataset_dir / "raw")
    if any(x is None for x in raw_data.values()):
        logger.warning(msg="Loading failed.")
        return "OUTPUT: Loading failed."

    # Data qualiti checks   
    logger.info(msg="Quality checks.")
    if not assert_data_quality(data=raw_data):
        logger.warning(msg="Data quality check failed.")
        return "OUTPUT: Data quality check failed."
    
    # Preprocess
    logger.info(msg="Intermediate dataframe")
    try:
        intermediate_pokemon_data = calculate_intermediate_df(raw_data=raw_data)
        if intermediate_pokemon_data is None:
            return "OUTPUT: Failed calculating intermediate dataframe."
    except Exception as e:
        logger.error(msg=e)
        logger.warning(msg="Failed calculating intermediate dataframe.")
        return "OUTPUT: Failed calculating intermediate dataframe."

    # Drop 
    logger.info(msg="Create staging dataframes")
    stg_data = calculate_staging_dfs(
        intermediate=intermediate_pokemon_data,
        pokedex=raw_data["raw_pokemon_index"]
    )
    if any(x is None for x in stg_data.values()):
        logger.warning(msg="Failed defining staging dataframes.")
        return "OUTPUT: Failed defining staging dataframes."
    
    # save csvs
    logger.info(msg="Save csvs")
    if not save_dataframes_dict(dfs=stg_data, dataset_dir=dataset_dir / "pipeline"):
        logger.warning(msg="Error in saving staging csvs.")
        return "OUTPUT: Error in saving staging csvs."

    # IF here, function worked
    logger.info(msg="End of preprocessing.")
    return "OUTPUT: Preprocess complete."


if __name__ == "__main__":
    main(dataset_dir=None)