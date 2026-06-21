from pydantic import BaseModel , Field
from enum import Enum


class FuelType(str,Enum):
    petrol="Petrol"
    diesel="Deisel"
    cng="CNG"

class SellerType(str,Enum):
    dealer = "Dealer"
    indivisual="Indivisual"

class TransmitionType(str,Enum):
    manual = "Manual"
    automatic = "Automatic"

class CarFeature(BaseModel):
    Car_Name: str = Field (...,example="ritz")
    Year : int = Field(...,example="2012")
    Present_Price : float =Field(...,example=8.99)
    Kms_Driven : int = Field(...,example="4002")
    Fuel_Type:FuelType
    Seller_Type:SellerType
    Transmission:TransmitionType
    Owner: int = Field(
        ...,ge=0, le=3 , example=0 , description="Number of previous owners"
    )


class PredictionResponse(BaseModel):
    predict_price: float
