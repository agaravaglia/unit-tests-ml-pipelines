
from pathlib import Path
import pandas as pd

from src.utilities.logging import Logger
from src.utilities.data import get_datset_dir, save_sklear_model, get_model_dir

from src.train.helpers import (
    load_features_datasets,
    train_model
)

logger = Logger(module="preprocess")


def main(dataset_dir: Path = None, model_dir: Path = None):
    """
    Main function of the preprocess.
    """
    logger.info(msg="Start executing preprocess module.")
    
    # Initialize dataset directory
    logger.info(msg="Get Directory.")
    if not dataset_dir:
        dataset_dir = get_datset_dir()
    if not model_dir:
        model_dir= get_model_dir()
    if not dataset_dir:
        logger.warning(msg="No dataset directory.")
        return "OUTPUT: No dataset directory."
    
    # Load data
    logger.info(msg="Load data.")
    features = load_features_datasets(dataset_folder=dataset_dir / "pipeline")
    if any(x is None for x in features.values()):
        logger.warning(msg="Loading failed.")
        return "OUTPUT: Loading failed."
    
    # Train model
    trained_classifier = train_model(data=features)
    if not trained_classifier:
        logger.warning(msg="Training failed.")
        return "OUTPUT: Training failed."
    
    # Save model
    if not save_sklear_model(
        obj=trained_classifier, 
        filename=(model_dir / "sklearn_classifier.joblib")
    ):
        logger.warning(msg="Model not saved.")
        return "OUTPUT: Model not saved."

    # IF here, function worked
    logger.info(msg="End of training.")
    return "OUTPUT: Training complete."


if __name__ == "__main__":
    main()