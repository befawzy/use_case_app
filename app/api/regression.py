from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from autoscout_use_case_app.app.model import RawCarDataRegression
from autoscout_use_case_app.app.utils.data_transform import (
    transform_data_regression,
    predict_detail_views,
)

router = APIRouter()


class PredictionRequest(BaseModel):
    data: RawCarDataRegression


@router.get("/")
def get_home():
    return {"message": "Welcome to the Regression Home"}


@router.post("/predict/")
def predict_reg(data: RawCarDataRegression):
    try:
        transformed_data = transform_data_regression(data)
        prediction_result = predict_detail_views(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
