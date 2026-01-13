import sys
import pandas as pd

print('arguments', sys.argv)

df = pd.DataFrame({"day": [1, 2], "fees": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print("Jalen brunson for president")