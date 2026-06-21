from fastapi import FastAPI
from schema import CarFeature , PredictionResponse
from model import load_artifacts , predict_price
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title="Car Price Prediction API", version="1,0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
