from app.model_loader import predict_logs


def test_prediction():

    logs = [
        "Application started",
        "OOMKilled"
    ]

    result = predict_logs(logs)

    assert len(result) == 2