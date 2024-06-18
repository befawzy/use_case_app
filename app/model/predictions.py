from pydantic import BaseModel


class ProductTierPrediction(BaseModel):
    product_tier: str


class DetailViewsPrediction(BaseModel):
    detail_views: int
