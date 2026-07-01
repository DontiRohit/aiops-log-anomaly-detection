from fastapi import FastAPI
from app.schemas import LogRequest
from app.model_loader import predict_log

app = FastAPI(title="AI Log Anomaly Detector")


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/predict")
def predict(request: LogRequest):
    return predict_log(request.log)