import pandas as pd, ta

def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy().sort_values("timestamp")
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    bband = ta.volatility.BollingerBands(df["close"])
    df["boll_high"] = bband.bollinger_hband()
    df["boll_low"]  = bband.bollinger_lband()
    df["target"] = df["close"].shift(-1)  # regression target
    return df.dropna()