import pandas as pd
from sqlalchemy import create_engine

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
df = pd.read_csv(url)

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df.head(n=0).to_sql(name='zones', con=engine, if_exists='replace')

print(pd.io.sql.get_schema(df, name='zones', con=engine))

df.to_sql(name='zones', con=engine, if_exists='append')