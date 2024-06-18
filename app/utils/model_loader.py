import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def load_classification_model(version):
    with open(
        f"{BASE_DIR}/trained_models/trained_pipeline-classification-{version}.pkl", "rb"
    ) as f:
        model = pickle.load(f)
    return model


def load_regression_model(version):
    with open(
        f"{BASE_DIR}/trained_models/trained_pipeline-regression-{version}.pkl", "rb"
    ) as f:
        model = pickle.load(f)
    return model
