import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create models directory
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sample_logs.csv")

# Convert logs to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["log"])

logging.info("Training started...")
# Train anomaly detection model
model = IsolationForest(
    contamination=0.30,
    random_state=42
)

model.fit(X)


logging.info("Model training completed.")


# Predict on training data
df["prediction"] = model.predict(X)

logging.info("Prediction counts:")
logging.info(df["prediction"].value_counts())



# Save model
joblib.dump(model, "models/anomaly_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

#print("✅ Model trained successfully!")
logging.info("Model saved successfully.")
logging.info("Vectorizer saved successfully.")

