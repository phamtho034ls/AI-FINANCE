import streamlit as st, requests, pandas as pd, plotly.graph_objects as go
API_URL = "http://localhost:8000/api/v1"

st.title("AI-Finance Dashboard")
symbol = st.selectbox("Symbol", ["BTCUSDT"])
if st.button("Get Signal"):
    resp = requests.get(f"{API_URL}/predict", params={"symbol": symbol})
    data = resp.json()
    st.write("Predicted next price:", data["predicted_price"])
    # Vẽ chart giả lập
    df = pd.read_csv("data/processed/BTCUSDT_processed.csv")[-100:]
    fig = go.Figure(data=[go.Candlestick(x=df["timestamp"],
                   open=df["open"], high=df["high"], low=df["low"], close=df["close"])])
    st.plotly_chart(fig)