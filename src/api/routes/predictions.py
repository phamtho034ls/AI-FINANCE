from fastapi import APIRouter, Query
from src.data_pipeline.collectors import fetch_binance_ohlcv
from src.data_pipeline.features import add_all_indicators
from src.models.registry import load_latest_model
import torch

router = APIRouter()

@router.get("/predict")
def predict(symbol: str = Query(...), lookback: int = 60):
    df = add_allicators(fetch_binance_ohlcv(symbol))[-lookback:]
    feat = df[["rsi","macd","boll_high","boll_low"]].values
    X = torch.tensor(feat, dtype=torch.float32).unsqueeze(0)  # (1,60,4)
    model, run_id = load_latest_model()
    model.eval()
    with torch.no_grad():
        pred = model(X).item()
    return {"symbol": symbol, "predicted_price": pred, "model_run_id": run_id}