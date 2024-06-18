from fastapi import FastAPI
import pickle
from pathlib import Path
from autoscout_use_case_app.app.model import RawCarDataClassification

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# assume we have a trained model
with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()


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
        - Handles optional columns (created_date, search_views, detail_views).
        - Calculates derived features like car_life, search_views_per_day, detail_views_per_day.
    """
    try:
        transformed_data = data.model_dump()  # Get a dictionary from the validated data

        # Handle optional columns
        if data.created_date:
            transformed_data["created_year"] = int(data.created_date.split("-")[0])
        if data.search_views:
            transformed_data["search_views_per_day"] = (
                data.search_views / transformed_data.get("stock_days", 1)
            )
        if data.detail_views:
            transformed_data["detail_views_per_day"] = (
                data.detail_views / transformed_data.get("stock_days", 1)
            )
        if data.created_date and data.first_registration_year:
            transformed_data["car_life"] = (
                transformed_data["created_year"] - data.first_registration_year
            )

        return transformed_data

    except Exception as e:
        raise ValueError(f"Error transforming data: {str(e)}")


from autoscout_use_case_app.app.model import RawCarDataRegression


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
        - Handles optional columns (created_date, search_views).
        - Assumes created_date is in YYYY-MM-DD format.
        - Calculates derived features like car_age.
    """
    try:
        transformed_data = data.model_dump()  # Convert Pydantic model to dictionary

        # Handle optional columns
        if data.created_date:
            transformed_data["created_year"] = int(data.created_date.split("-")[0])
        if data.search_views:
            transformed_data["search_views_per_day"] = (
                data.search_views / transformed_data.get("stock_days", 1)
            )
        if data.created_date and data.first_registration_year:
            transformed_data["car_life"] = (
                transformed_data["created_year"] - data.first_registration_year
            )

        return transformed_data

    except Exception as e:
        raise ValueError(f"Error transforming data: {str(e)}")


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
    prediction = model.predict([transformed_data])[0]

    # Map numeric prediction to product tier
    product_tier = {0: "Basic", 1: "Plus", 2: "Premium"}.get(prediction, "Unknown")

    return {"predicted_class": product_tier}


def predict_detail_views(model, transformed_data: dict) -> float:
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
        prediction = model.predict([transformed_data])[0]
        return float(prediction)  # Convert to float if necessary
    except Exception as e:
        raise ValueError(f"Error predicting regression: {str(e)}")
