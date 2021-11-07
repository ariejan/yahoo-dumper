import yfinance as yf
from pathlib import Path
import json

# Make sure our output dir exists
output_dir = "data"
Path(output_dir).mkdir(exist_ok=True)

with open("tickers.txt", "r") as tickers:
    for raw_ticker in tickers:
        ticker = raw_ticker.strip()

        print("Loading data for " + ticker)

        data = yf.Ticker(ticker)
        history = data.history(period="max")

        print("Writing data for " + ticker)
        history.to_json(path_or_buf=output_dir + "/" + ticker + ".json", orient="table")
