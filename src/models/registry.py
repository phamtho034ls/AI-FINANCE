import mlflow, torch
from src.config import MLFLOW_TRACKING_URI

def load_latest_model():
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    client = mlflow.tracking.MlflowClient()
    run_info = client.search_runs(experiment_ids=["0"], order_by=["start_time DESC"])[0]
    model_uri = f"runs:/{run_info.info.run_id}/model"
    model = mlflow.pytorch.load_model(model_uri)
    return model, run_info.info.run_id