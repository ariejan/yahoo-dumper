# Yahoo Dumper

Quick python script to download historical ticker data from Yahoo Finance. Of course, for personal use only. 

# Requirements

Python 3.x and everything from `requirements.txt`:

```
pip install -r requirements.txt
```

# Usage

Edit `tickers.txt` to select the tickers you need. The default contains a snapshot of S&P 500 tickers. Then run:

```
python yahoo.py
```

All historical data will be saved in a `data` subdirectory in JSON format. Note that this a simple serialization 
of a Pandas DataFrame, so there is some meta data. The core data lives in the `"data"` field:

```
{
  "schema": {
    "fields": [
      # ... omitted
    ],
    "primaryKey": [
      "Date"
    ],
    "pandas_version": "0.20.0"
  },
  "data": [
    {
      "Date": "1980-12-12T00:00:00.000Z",
      "Open": 0.1004534587,
      "High": 0.1008901887,
      "Low": 0.1004534587,
      "Close": 0.1004534587,
      "Volume": 469033600,
      "Dividends": 0,
      "Stock Splits": 0
    },
    # ... omitted
  ]
}
```
