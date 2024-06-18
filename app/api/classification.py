from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from autoscout_use_case_app.app.model import RawCarDataClassification
from autoscout_use_case_app.app.utils.data_transform import (
    transform_data_classification,
    predict_tier_classification,
)

router = APIRouter()


class PredictionRequest(BaseModel):
    data: RawCarDataClassification


@router.get("/")
def get_home():
    return {"message": "This is the Product Tier Classification Home Page"}


@router.post("/predict/")
def predict_class(data: RawCarDataClassification):
    try:
        transformed_data = transform_data_classification(data)
        prediction_result = predict_tier_classification(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
