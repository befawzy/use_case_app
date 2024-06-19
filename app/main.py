from fastapi import FastAPI
from app.routers import classification, regression

app = FastAPI()


@app.get("/")
def get_home():
    return {"message": "This is the use case app Home Page"}


app.include_router(
    classification.router, prefix="/classification", tags=["Classification"]
)
app.include_router(regression.router, prefix="/regression", tags=["Regression"])
