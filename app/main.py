from fastapi import FastAPI
from autoscout_use_case_app.app.api import classification, regression

app = FastAPI()

app.include_router(
    classification.router, prefix="/classification", tags=["Classification"]
)
app.include_router(regression.router, prefix="/regression", tags=["Regression"])
