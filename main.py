from fastapi import FastAPI
from schema import CarFeature , PredictionResponse
from model import load_artifacts , predict_price
from fastapi.responses import JSONResponse


app=FastAPI(title="Car Price Prediction API", version="1,0")


@app.on_event("startup")
def startup_event():
    load_artifacts()
    

@app.get("/")
def test():
    return JSONResponse(
        status_code=201,
        content={
            "success":True, "message":"this is test route"
        }
    )


@app.post("/product",response_model=PredictionResponse)
def prediction(features : CarFeature):
    price=predict_price(features.model_dump())
    return PredictionResponse(predict_price=price)