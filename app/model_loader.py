import joblib

model = joblib.load("models/anomaly_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_log(log: str):
    vector = vectorizer.transform([log])
    prediction = model.predict(vector)[0]

    return {
        "log": log,
        "status": "Anomaly" if prediction == -1 else "Normal"
    }