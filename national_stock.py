import yfinance as yf
import pandas as pd

indices = {
    "ATX": "^ATX",
    "DAX": "^GDAXI",
    "CAC": "^FCHI"
}

data = {}

for name, ticker in indices.items():
    index = yf.Ticker(ticker)
    data[name] = index.history(period="1y")  # Fetch 1 year of data

df = pd.concat(data, axis=1)
df.to_csv("indices_data.csv")  # Save data to CSV
