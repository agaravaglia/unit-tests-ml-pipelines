from typing import Dict, Optional, List

import pandas as pd
import numpy as np
from sklearn.datasets import make_classification


def classification_table(
    n_samples: int,
    n_features: int,
    feature_names: List[str] = [],
    target_name: str = "is_legendary"
) -> Dict[str, pd.DataFrame]:
    """
    Create dataset
    """
    np.random.seed(100)

    # Check feature name and number
    if not feature_names or len(feature_names) != n_features:
        feature_names = feature_names_default(n_features=n_features)
    
    # simulate dataset
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_features,
        n_redundant=0,
        n_repeated=0,
        random_state=100
    )
    
    return {
        "features": pd.DataFrame(X, columns=feature_names),
        "target": pd.DataFrame(y, columns=[target_name]),
    }


def feature_names_default(n_features: int):
    return [f"feat_{i}" for i in range (1, n_features + 1)]
