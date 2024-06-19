from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data_models import RawCarDataRegression
from app.utils.data_transform import (
    transform_data_regression,
    predict_detail_views,
)

router = APIRouter()


class PredictionRequest(BaseModel):
    data: RawCarDataRegression


@router.post("/detail_views_regression/")
def predict_reg(data: RawCarDataRegression):
    try:
        transformed_data = transform_data_regression(data)
        prediction_result = predict_detail_views(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
