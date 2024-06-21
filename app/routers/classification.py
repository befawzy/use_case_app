from fastapi import APIRouter, HTTPException
from app.data_models import RawCarDataClassification, ProductTierPrediction
from app.utils.data_transform import (
    transform_data_classification,
    predict_tier_classification,
)

router = APIRouter()


@router.post("/product_tier_classification/", response_model=ProductTierPrediction)
def predict_class(data: RawCarDataClassification):
    try:
        transformed_data = transform_data_classification(data)
        prediction_result = predict_tier_classification(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
