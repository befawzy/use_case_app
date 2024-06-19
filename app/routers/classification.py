from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data_models import RawCarDataClassification
from app.utils.data_transform import (
    transform_data_classification,
    predict_tier_classification,
)

router = APIRouter()


class PredictionRequest(BaseModel):
    data: RawCarDataClassification


@router.post("/product_tier_classification/")
def predict_class(data: RawCarDataClassification):
    try:
        transformed_data = transform_data_classification(data)
        prediction_result = predict_tier_classification(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
