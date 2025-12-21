import mlflow
import mlflow.sklearn

def log_model(model, metrics: dict):
    mlflow.start_run()
    for k, v in metrics.items():
        mlflow.log_metric(k, v)
    mlflow.sklearn.log_model(model, "model")
    mlflow.end_run()
