import pandas as pd
from sqlalchemy import create_engine
import pymysql

df = pd.read_csv('data.csv')

engine = create_engine("mysql+pymysql://root:Huyhuy2005@localhost:3306/Apple_stock_price")

df.to_sql("Apple_stock_price", engine, if_exists='replace', index=False)

print('Done!')
