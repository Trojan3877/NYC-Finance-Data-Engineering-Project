from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="NYC Finance ML Inference API")

# Load trained model (example)
model = joblib.load("models/model.pkl")

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}
