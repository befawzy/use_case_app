from pydantic import BaseModel, Field
from typing import Optional, Annotated


class RawCarDataClassification(BaseModel):
    make_name: Annotated[str, Field(min_length=1)]
    price: int
    first_zip_digit: int
    first_registration_year: int
    stock_days: int
    created_date: str
    search_views: int
    detail_views: int
    ctr: float

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "make_name": "VW",
                "price": 64605,
                "first_zip_digit": 8,
                "first_registration_year": 2015,
                "stock_days": 0,
                "created_date": "2023-06-25",
                "search_views": 100,
                "detail_views": 50,
            }
        }
