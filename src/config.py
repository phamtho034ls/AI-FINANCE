import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_URL   = os.getenv("BINANCE_URL", "https://api.binance.com")
VNDIRECT_URL  = os.getenv("VNDIRECT_URL", "https://dchart-api.vndirect.com.vn")
DATABASE_URL  = os.getenv("DATABASE_URL", "sqlite:///finance.db")
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlruns.db")