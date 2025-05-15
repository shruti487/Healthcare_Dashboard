import pandas as pd

df = pd.read_csv("./Data/raw_data.csv", header=None)
print(f"Number of columns: {df.shape[1]}")
print(df.head())
