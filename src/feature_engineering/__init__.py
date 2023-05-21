from pathlib import Path
from typing import Optional
import pandas as pd

from src.utilities.logging import Logger
from src.utilities.data import get_datset_dir

from src.utilities.data import save_dataframes_dict
from src.feature_engineering.helpers import (
    load_stg_datasets,
    calculate_features_and_target
)

logger = Logger(module="feature_engineering")


def main(dataset_dir: Optional[Path] = None):
    """
    Main function of the Feature engineering.
    """
    logger.info(msg="Start executing preprocess module.")
    
    # Initialize dataset directory
    logger.info(msg="Get Directory.")
    if not dataset_dir:
        dataset_dir = get_datset_dir() 
    if not dataset_dir:
        logger.warning(msg="No dataset directory.")
        return "OUTPUT: No dataset directory."
    
    # Load data
    logger.info(msg="Load data.")
    stg_data = load_stg_datasets(dataset_dir=dataset_dir / "pipeline") 
    if any(x is None for x in stg_data.values()):
        logger.warning(msg="Loading failed.")
        return "OUTPUT: Loading failed."

    #Calcuate features
    logger.info(msg="Calculate features")
    features = calculate_features_and_target(stg_data=stg_data)
    if not features or any(x is None for x in features.values()):
        logger.warning(msg="Failed computing features.")
        return "OUTPUT: Failed computing features."
    
    # save csvs
    logger.info(msg="Save csvs")
    if not save_dataframes_dict(dfs=features, dataset_dir=dataset_dir / "pipeline"):
        logger.warning(msg="Error in saving features csvs.")
        return "OUTPUT: Error in saving features csvs."

    # IF here, function worked
    logger.info(msg="End of preprocessing.")
    return "OUTPUT: Feature engineering complete."


if __name__ == "__main__":
    main()