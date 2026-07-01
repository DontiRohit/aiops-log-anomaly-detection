import joblib

# Load model
model = joblib.load("models/anomaly_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

logs = [
    "Application started",
    "Health check passed",
    "OOMKilled",
    "Kernel panic occurred",
    "Connected to database",
    "Segmentation fault"
]

X = vectorizer.transform(logs)

predictions = model.predict(X)

for log, prediction in zip(logs, predictions):
    status = "Anomaly" if prediction == -1 else "Normal"
    print(f"{log:<30} {status}")