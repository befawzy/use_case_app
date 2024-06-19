import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def load_classification_model(version):
    with open(
        f"{BASE_DIR}/trained_models/product_tier_prediction-{version}.pkl", "rb"
    ) as f:
        product_tier_classifier = pickle.load(f)
    return product_tier_classifier


def load_regression_model(version):
    with open(
        f"{BASE_DIR}/trained_models/detail_views_regression-{version}.pkl", "rb"
    ) as f:
        detail_views_regressor = pickle.load(f)
    return detail_views_regressor
