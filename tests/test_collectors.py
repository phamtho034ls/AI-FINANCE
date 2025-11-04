from src.data_pipeline.collectors import fetch_binance_ohlcv

def test_fetch():
    df = fetch_binance_ohlcv("BTCUSDT", limit=10)
    assert not df.empty
    assert list(df.columns) == ["timestamp","open","high","low","close","volume"]
    