from src.data_pipeline.collectors import fetch_binance_ohlcv
from src.data_pipeline.features import add_all_indicators
import os, pandas as pd

symbol = "BTCUSDT"
raw_path = f"data/raw/{symbol}.csv"
proc_path = f"data/processed/{symbol}_processed.csv"

df = fetch_binance_ohlcv(symbol)
df.to_csv(raw_path, index=False)

df_feat = add_all_indicators(df)
df_feat.to_csv(proc_path, index=False)
print("ETL done:", proc_path)