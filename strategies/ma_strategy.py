def decide(df_row):
    # expects row with ma20, ma50, Close
    if df_row["ma20"] > df_row["ma50"]:
        return "buy"
    elif df_row["ma20"] < df_row["ma50"]:
        return "sell"
    return "hold"
