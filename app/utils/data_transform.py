from datetime import datetime
import pandas as pd
from pathlib import Path
from app.data_models import RawCarDataClassification, RawCarDataRegression
import logging
from .model_loader import load_classification_model, load_regression_model

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


def transform_data_classification(data: RawCarDataClassification) -> dict:
    """
    Transforms user data based on the RawCarData schema and model requirements.

    Args:
        data: User-provided data in RawCarData format.

    Returns:
        A dictionary containing transformed data ready for the model.

    Raises:
        ValueError: If required fields are missing or invalid.

    Notes:
        - Assumes created_date is in YYYY-MM-DD format.
        - Calculates derived features like car_life, search_views_per_day, detail_views_per_day.
    """
    try:
        transformed_data = data.model_dump()

        transformed_data["created_date"] = datetime.strptime(
            transformed_data["created_date"], "%Y-%m-%d"
        )
        transformed_data["daily_search_views"] = transformed_data[
            "search_views"
        ] / transformed_data.get("stock_days", 1)

        transformed_data["daily_detail_views"] = transformed_data[
            "detail_views"
        ] / transformed_data.get("stock_days", 1)

        transformed_data["car_life"] = (
            transformed_data["created_date"].year
            - transformed_data["first_registration_year"]
        )

        return transformed_data

    except Exception as e:
        logger.error(f"Error transforming classification data: {e}")
        raise ValueError(f"Error transforming classification data: {str(e)}")


def transform_data_regression(data: RawCarDataRegression) -> dict:
    """
    Transforms user data based on the RawCarDataRegression schema and model requirements.

    Args:
        data: User-provided data in RawCarDataRegression format.

    Returns:
        A dictionary containing transformed data ready for the regression model.

    Raises:
        ValueError: If required fields are missing or invalid.

    Notes:
        - Assumes created_date is in YYYY-MM-DD format.
        - Calculates derived features like car_age.
    """
    try:
        transformed_data = data.model_dump()  # Convert Pydantic model to dictionary

        # Handle optional columns
        transformed_data["created_date"] = datetime.strptime(
            transformed_data["created_date"], "%Y-%m-%d"
        )
        transformed_data["daily_search_views"] = transformed_data[
            "search_views"
        ] / transformed_data.get("stock_days", 1)
        transformed_data["car_life"] = (
            transformed_data["created_date"].year
            - transformed_data["first_registration_year"]
        )

        return transformed_data

    except Exception as e:
        logger.error(f"Error transforming regression data: {e}")
        raise ValueError(f"Error transforming regression data: {str(e)}")


def predict_tier_classification(transformed_data: dict) -> dict:
    """
    Predicts classification using the trained model based on transformed data.

    Args:
        transformed_data: Dictionary containing transformed data ready for the model.

    Returns:
        A dictionary containing the predicted class (product tier).
    """
    # Handle potential missing required data that might affect prediction
    required_features = [
        "make_name",
        "price",
        "first_zip_digit",
        "first_registration_year",
    ]
    for feature in required_features:
        if feature not in transformed_data:
            return {"error": f"Missing required feature: {feature}"}
    # Make prediction using the transformed data
    try:
        transformed_df = pd.DataFrame([transformed_data])
        product_tier_classifier = load_classification_model(__version__)
        prediction = product_tier_classifier.predict(transformed_df)[0]

        # Map numeric prediction to product tier
        product_tier = {0: "Basic", 1: "Plus", 2: "Premium"}.get(prediction, "Unknown")
        return {"predicted_class": product_tier}
    except Exception as e:
        logger.error(f"Error during classification: {e}")
        raise ValueError(f"Error during classification: {str(e)}")


def predict_detail_views(transformed_data: dict) -> float:
    """
    Predicts regression output using the trained model and transformed data.

    Args:
        model: Trained regression model (e.g., RandomForestRegressor, XGBRegressor).
        transformed_data: Dictionary containing transformed data ready for prediction.

    Returns:
        Float prediction based on the regression model.
    """
    try:
        # Make prediction using the transformed data
        transformed_df = pd.DataFrame([transformed_data])
        detail_views_regressor = load_regression_model(__version__)
        prediction = detail_views_regressor.predict(transformed_df)[0]
        return float(prediction)  # Convert to float if necessary
    except Exception as e:
        raise ValueError(f"Error predicting regression: {str(e)}")
