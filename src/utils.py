import pandas as pd

# Load parquet file
df = pd.read_parquet("tweets.parquet")

# Display first 10 rows
print(df.head(10))