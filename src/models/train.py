import mlflow, torch, torch.nn as nn
from src.data_pipeline.collectors import fetch_binance_ohlcv
from src.data_pipeline.features import add_all_indicators
from src.models.lstm_net import LSTMNet  # file bên dưới

def build_xy(df, lookback=60):
    feat = df[["rsi","macd","boll_high","boll_low"]].values
    X, y = [], []
    for i in range(lookback, len(feat)):
        X.append(feat[i-lookback:i])
        y.append(df["target"].iloc[i])
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32).view(-1,1)

def train(symbol="BTCUSDT", lookback=60, epochs=20):
    df = add_all_indicators(fetch_binance_ohlcv(symbol))
    X, y = build_xy(df, lookback)
    model = LSTMNet(input_size=X.shape[2])
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    with mlflow.start_run():
        for epoch in range(epochs):
            model.train()
            pred = model(X)
            loss = criterion(pred, y)
            optimizer.zero_grad(); loss.backward(); optimizer.step()
            mlflow.log_metric("loss", loss.item(), step=epoch)
        mlflow.pytorch.log_model(model, "model")
        print("Saved model to MLflow, run_id:", mlflow.active_run().info.run_id)

if __name__ == "__main__":
    train()