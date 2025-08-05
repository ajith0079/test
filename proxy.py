import pandas as pd
from sqlalchemy 
import create_engine

df = pd.read_csv('Company_S&HQ.csv')
engine = create_engine('postgresql://user:pass@localhost:ABCDABCD1234$/seqlstocks')

df.to_sql('companies', engine, if_exists='append', index=False)