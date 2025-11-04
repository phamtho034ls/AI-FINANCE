import requests, pandas as pd
from src.config import BINANCE_URL

def fetch_binance_ohlcv(symbol: str = "BTCUSDT", interval: str = "15m", limit: int = 500) -> pd.DataFrame:
    url = BINANCE_URL + "/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data, columns=["t","o","h","l","c","v","T","q","n","V","Q","Y"])
    df = df[["t","o","h","l","c","v"]].astype(float)
    df.columns = ["timestamp","open","high","low","close","volume"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df