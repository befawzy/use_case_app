import pytest
from pydantic import ValidationError
from app.data_models import RawCarDataRegression

def test_valid_raw_car_data_regression():
    valid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 8,
        "first_registration_year": 2020,
        "stock_days": 10,
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    try:
        data = RawCarDataRegression(**valid_data)
    except ValidationError:
        pytest.fail("Valid data raised ValidationError")

def test_invalid_price_regression():
    invalid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": -80000.0,  # Invalid price
        "first_zip_digit": 8,
        "first_registration_year": 2020,
        "stock_days": 10,
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)

def test_invalid_first_zip_digit_regression():
    invalid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 10,  # Invalid first_zip_digit
        "first_registration_year": 2020,
        "stock_days": 10,
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)

def test_invalid_first_registration_year_regression():
    invalid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 8,
        "first_registration_year": 1900,  # Invalid first_registration_year
        "stock_days": 10,
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)

def test_invalid_created_date_regression():
    invalid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 8,
        "first_registration_year": 2020,
        "stock_days": 10,
        "created_date": "2024/06/01",  # Invalid created_date
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)

def test_invalid_stock_days_regression():
    invalid_data = {
        "product_tier": "Plus",
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 8,
        "first_registration_year": 2020,
        "stock_days": -1,  # Invalid stock_days
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)

def test_invalid_product_tier_regression():
    invalid_data = {
        "product_tier": "",  # Invalid product_tier
        "make_name": "BMW",
        "price": 80000.0,
        "first_zip_digit": 8,
        "first_registration_year": 2020,
        "stock_days": 10,
        "created_date": "2024-06-01",
        "search_views": 100,
        "ctr": 2.0,
    }
    with pytest.raises(ValidationError):
        RawCarDataRegression(**invalid_data)
