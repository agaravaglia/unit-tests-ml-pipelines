from pathlib import Path
import pandas as pd

from src.utilities.logging import Logger
from src.utilities.data import (
    get_datset_dir,
    load_sklear_model,
    save_dataframes_dict,
    get_model_dir
)

from src.predict.helpers import (
    load_features_datasets,
    batch_prediction
)

logger = Logger(module="predict")


def main(dataset_dir: Path = None, model_dir: Path = None):
    """
    Main function of the preprocess.
    """
    logger.info(msg="Start executing prediction module.")
    
    # Initialize dataset directory
    logger.info(msg="Get Directory.")
    if not dataset_dir:
        dataset_dir = get_datset_dir()
    if not model_dir:
        model_dir = get_model_dir()
    if not dataset_dir or not model_dir:
        logger.warning(msg="No dataset directory.")
        return "OUTPUT: No dataset directory."
    
    # Load data
    logger.info(msg="Load data.")
    features = load_features_datasets(dataset_folder=dataset_dir / "pipeline")
    if any(x is None for x in features.values()):
        logger.warning(msg="Loading data failed.")
        print(features)
        return "OUTPUT: Loading data failed."

    # Train model
    trained_classifier = load_sklear_model(filename=model_dir / "sklearn_classifier.joblib")
    if not trained_classifier:
        logger.warning(msg="Loading model failed.")
        return "OUTPUT: Loading model failed."
    
    # Make predictions
    logger.info(msg="Make predictions")
    predictions = batch_prediction(classifier=trained_classifier, data=features)
    if not predictions:
        logger.warning(msg="Predictions failed.")
        return "OUTPUT: Predictions failed."

    # save csvs
    logger.info(msg="Save csvs")
    if not save_dataframes_dict(dfs=predictions, dataset_dir=dataset_dir / "pipeline"):
        logger.warning(msg="Error in saving prediction csvs.")
        return "OUTPUT: Error in saving predictions csvs."

    # IF here, function worked
    logger.info(msg="End of training.")
    return "OUTPUT: Predict complete."


if __name__ == "__main__":
    main()