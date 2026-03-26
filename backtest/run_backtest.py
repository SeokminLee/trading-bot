import pandas as pd
import yfinance as yf


def run_backtest(ticker="AAPL"):
    print(f"Running simple backtest for {ticker}")
    data = yf.download(ticker, period="1y", interval="1d")
    if data.empty:
        print("No data")
        return
    data["ma20"] = data["Close"].rolling(20).mean()
    data["ma50"] = data["Close"].rolling(50).mean()
    data = data.dropna()
    cash = 10000
    position = 0
    equity = []
    for idx, row in data.iterrows():
        if row["ma20"] > row["ma50"] and position == 0:
            position = cash / row["Close"]
            cash = 0
            print(f"buy at {row.name.date()} price {row.Close}")
        elif row["ma20"] < row["ma50"] and position > 0:
            cash = position * row["Close"]
            position = 0
            print(f"sell at {row.name.date()} price {row.Close}")
        equity.append(cash + position * row["Close"])
    print("Final equity", equity[-1])
    return equity
