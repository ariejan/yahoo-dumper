import os
import json
from pathlib import Path
import yfinance as yf

# Make sure our output dir exists
output_dir = "data"
Path(output_dir).mkdir(exist_ok=True)

with open("tickers.txt", "r") as tickers:
    for raw_ticker in tickers:
        ticker = raw_ticker.strip()
        output_file = output_dir + "/" + ticker + ".json"

        if os.path.isfile(output_file):
            print("Skipping data for " + ticker)
        else:
            print("Fetching data for " + ticker)
            data = yf.Ticker(ticker)
            history = data.history(period="max")

            history.to_json(path_or_buf=output_file, orient="table")
