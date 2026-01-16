import pandas as pd

url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'

df = pd.read_parquet(url)


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df.head(n=0).to_sql(name='green_taxi_data', con=engine, if_exists='replace')
print(pd.io.sql.get_schema(df, name='green_taxi_data', con=engine))
df.to_sql(name='green_taxi_data', con=engine, if_exists='append')
