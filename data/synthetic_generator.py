import pandas as pd
import numpy as np

def generate(size=100000):
    df = pd.DataFrame({
        "timestamp": pd.date_range(start="2020-01-01", periods=size, freq="H"),
        "stock_price": np.random.normal(100, 5, size),
        "volume": np.random.randint(1000, 500000, size),
        "open": np.random.normal(100, 5, size),
        "close": np.random.normal(100, 5, size),
        "sector": np.random.choice(["Tech","Finance","Health"], size)
    })
    df.to_csv("data/raw/nyc_finance_synthetic.csv", index=False)
