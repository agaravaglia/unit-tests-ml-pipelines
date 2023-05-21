from functools import partial
from typing import Dict, Any

from hyperopt import hp, fmin, tpe, STATUS_OK, space_eval
from hyperopt import Trials
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

from src.utilities.logging import Logger

logger = Logger(module="train.tuning")

HYPERSPACE = {
    "penalty": hp.choice("penalty", ["l1", "l2"]),
    "class_weight": hp.choice("class_weight", ["balanced", None]),
    "max_iter": hp.choice("max_iter", [100, 300, 500, 600, 1000, 1500, 2000]),
    "fit_intercept": hp.choice("fit_intercept", [True, False]),
    "solver": hp.choice("solver", ["saga", "liblinear"]),
}


def objective_function(
    hyperparameters: Dict[str, Any], 
    X: pd.DataFrame, 
    y: pd.DataFrame, 
) -> Dict[str, Any]:
    """
    train single instance
    """
    try:
        np.random.seed(100)
        
        # Initialize 
        classifier = LogisticRegression(**hyperparameters)
        
        # get scores via cross validation
        logger.info("Make cross validation")
        scores = cross_val_score(
            classifier, X, y.values.reshape(y.shape[0], ), cv=5, scoring='f1'
        )
        print(scores)
    except Exception as e:
        logger.error(e)
        scores = [-1]

    # return value
    return {
        "loss": -np.mean(scores),
        "hyperparameters": hyperparameters,
        'status': STATUS_OK
    }
    

def tune_hyperparameters(
    X: pd.DataFrame,
    y: pd.DataFrame,
    max_evals: int = 10
):
    """
    Function that returns the dictionary of best hyperparameters
    """
    np.random.seed(100)
    # initialize trials and 
    trials = Trials()

    logger.info(msg="Start tuning hyperparameters")
    best_result = fmin(
        partial(objective_function, X=X, y=y),
        space=HYPERSPACE,
        algo=tpe.suggest,
        max_evals=max_evals,
        trials=trials,
        rstate=np.random.default_rng(100)
    )
    logger.info(msg="Done tuning.")
    output = space_eval(HYPERSPACE, best_result)
    print("OUTPUT", output)
    return output