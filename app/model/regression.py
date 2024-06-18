from pydantic import BaseModel, Field
from typing import Optional, Annotated


class RawCarDataRegression(BaseModel):
    product_tier: Annotated[str, Field(min_length=1)]
    make_name: Annotated[str, Field(min_length=1)]
    price: int
    first_zip_digit: int
    first_registration_year: int
    stock_days: int
    created_date: Optional[str]
    deleted_date: Optional[str]
    search_views: Optional[float]
    ctr: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "product_tier": "Plus",
                "make_name": "BMW",
                "price": 80000,
                "first_zip_digit": 8,
                "first_registration_year": 2020,
                "stock_days": 0,
            }
        }
