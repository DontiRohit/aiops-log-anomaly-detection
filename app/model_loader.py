import joblib

model = joblib.load("models/anomaly_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_logs(logs):

    vectors = vectorizer.transform(logs)

    predictions = model.predict(vectors)

    results = []

    for log, prediction in zip(logs, predictions):

        results.append({
            "log": log,
            "status": "Anomaly" if prediction == -1 else "Normal"
        })

    return results