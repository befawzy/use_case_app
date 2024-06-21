from fastapi import APIRouter, HTTPException
from app.data_models import RawCarDataRegression, DetailViewsPrediction
from app.utils.data_transform import (
    transform_data_regression,
    predict_detail_views,
)

router = APIRouter()


@router.post("/detail_views_regression/", response_model=DetailViewsPrediction)
def predict_reg(data: RawCarDataRegression):
    try:
        transformed_data = transform_data_regression(data)
        prediction_result = predict_detail_views(transformed_data)
        return prediction_result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
