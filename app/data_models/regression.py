from datetime import datetime
from pydantic import BaseModel, Field, validator
from pydantic.types import Annotated, StringConstraints


class RawCarDataRegression(BaseModel):
    product_tier: Annotated[str, Field(min_length=1)]
    make_name: Annotated[str, Field(min_length=1)]
    price: Annotated[float, Field(gt=0)]
    first_zip_digit: Annotated[int, Field(ge=0, le=9)]
    first_registration_year: int
    stock_days: Annotated[int, Field(gt=0)]
    created_date: Annotated[str, StringConstraints(pattern=r"^\d{4}-\d{2}-\d{2}$")]
    search_views: Annotated[int, Field(gt=0)]
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
