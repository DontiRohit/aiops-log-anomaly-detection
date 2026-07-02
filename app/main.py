from fastapi import FastAPI
from app.schemas import LogRequest
from app.model_loader import predict_log
from app.elastic import get_logs
from app.model_loader import predict_logs

app = FastAPI(title="AI Log Anomaly Detector")


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/predict")
def predict(request: LogRequest):
    return predict_log(request.log)


@app.get("/detect")
def detect():

    logs = get_logs()

    return predict_logs(logs)