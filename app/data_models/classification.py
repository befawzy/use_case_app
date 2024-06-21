from datetime import datetime
from pydantic import BaseModel, Field, validator
from pydantic.types import StringConstraints
from typing import Annotated


class RawCarDataClassification(BaseModel):
    make_name: Annotated[str, Field(min_length=1)]
    price: Annotated[float, Field(gt=0)]
    first_zip_digit: Annotated[int, Field(ge=0, le=9)]
    first_registration_year: int
    stock_days: Annotated[int, Field(gt=0)]
    created_date: Annotated[str, StringConstraints(pattern=r"^\d{4}-\d{2}-\d{2}$")]
    search_views: Annotated[int, Field(gt=0)]
    detail_views: Annotated[int, Field(ge=0)]
    ctr: float

    @validator("first_registration_year")
    def year_range(cls, v):
        current_year = datetime.now().year
        min_year = current_year - 50  # 50 years ago, this is to be tuned as required
        max_year = current_year  # Current year

        if v < min_year or v > max_year:
            raise ValueError(
                f"first_registration_year must be between {min_year} and {max_year}"
            )

        return v

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "make_name": "VW",
                "price": 64605,
                "first_zip_digit": 8,
                "first_registration_year": 2015,
                "stock_days": 10,
                "created_date": "2023-06-25",
                "search_views": 100,
                "detail_views": 50,
                "ctr": 2.0,
            }
        }
