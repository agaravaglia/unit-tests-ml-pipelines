from typing import Optional, Dict, Any

from sklearn.linear_model import LogisticRegression


def check_model(
    model: Optional[LogisticRegression],
    expected_model: Optional[Dict[str, Any]]
):
    """
    Verify that model is as expected
    """
    try:
        assert isinstance(model, LogisticRegression)
        assert model.feature_names_in_.tolist() == expected_model["feature_names_in_"]
        assert model.n_features_in_ == expected_model["n_features_in_"]
    except:
        assert model is None
        assert expected_model is None