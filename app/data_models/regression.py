from pydantic import BaseModel, Field
from typing import Optional, Annotated


class RawCarDataRegression(BaseModel):
    product_tier: Annotated[str, Field(min_length=1)]
    make_name: Annotated[str, Field(min_length=1)]
    price: int
    first_zip_digit: int
    first_registration_year: int
    stock_days: int
    created_date: str
    search_views: int
    ctr: float

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "product_tier": "Plus",
                "make_name": "BMW",
                "price": 80000,
                "first_zip_digit": 8,
                "first_registration_year": 2020,
                "stock_days": 0,
                "created_date": "2024-06-01",
                "search_views": 100,
                "stock_days": 10,
                "ctr": 2.0,
            }
        }
