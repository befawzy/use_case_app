import pytest
from pydantic import ValidationError
from app.data_models import RawCarDataClassification

def test_valid_raw_car_data_classification():
    valid_data = {
        "make_name": "VW",
        "price": 64605.0,
        "first_zip_digit": 8,
        "first_registration_year": 2015,
        "stock_days": 10,
        "created_date": "2023-06-25",
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    try:
        _ = RawCarDataClassification(**valid_data)
    except ValidationError:
        pytest.fail("Valid data raised ValidationError")

def test_invalid_raw_car_data_classification_price():
    invalid_data = {
        "make_name": "VW",
        "price": -10.0,  # Invalid price
        "first_zip_digit": 8,
        "first_registration_year": 2015,
        "stock_days": 10,
        "created_date": "2023-06-25",
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataClassification(**invalid_data)

def test_invalid_first_zip_digit_classification():
    invalid_data = {
        "make_name": "VW",
        "price": 64605.0,
        "first_zip_digit": 10,  # Invalid first_zip_digit
        "first_registration_year": 2015,
        "stock_days": 10,
        "created_date": "2024-06-24",
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataClassification(**invalid_data)

def test_invalid_first_registration_year_classification():
    invalid_data = {
        "make_name": "VW",
        "price": 64605.0,
        "first_zip_digit": 8,
        "first_registration_year": 1900,  # Invalid first_registration_year
        "stock_days": 10,
        "created_date": "2023-06-24",
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataClassification(**invalid_data)

def test_invalid_created_date_classification():
    invalid_data = {
        "make_name": "VW",
        "price": 64605.0,
        "first_zip_digit": 8,
        "first_registration_year": 2015,
        "stock_days": 10,
        "created_date": "2023-06-25T00:00:00",  # Invalid created_date
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataClassification(**invalid_data)

def test_invalid_stock_days_classification():
    invalid_data = {
        "make_name": "VW",
        "price": 64605.0,
        "first_zip_digit": 8,
        "first_registration_year": 2015,
        "stock_days": -1,  # Invalid stock_days
        "created_date": "2024-06-25",
        "search_views": 100,
        "detail_views": 50,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataClassification(**invalid_data)
