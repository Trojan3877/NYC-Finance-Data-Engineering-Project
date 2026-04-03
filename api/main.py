from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import os

app = FastAPI(title="NYC Finance ML Inference API")

# Lazy-loaded model — avoids a hard crash at startup when the model file
# has not been generated yet.
_model = None


def _get_model():
    global _model
    if _model is None:
        import joblib

        model_path = os.environ.get("MODEL_PATH", os.path.join("models", "model.pkl"))
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found at '{model_path}'. "
                "Train the model first and ensure MODEL_PATH is set correctly."
            )
        _model = joblib.load(model_path)
    return _model


class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    try:
        model = _get_model()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}
