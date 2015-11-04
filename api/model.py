import sqlsoup
import os

PG_USER = os.environ['PG_USER']
PG_PASS = os.environ['PG_PASSWORD']
PG_HOST = os.environ['PG_HOST']
PG_DBNAME = os.environ['PG_DBNAME']


#connection template
ct = "postgresql://{}:{}@{}/{}"

#connection string 
cs = ct.format(PG_USER,PG_PASS,PG_HOST,PG_DBNAME)
db  = sqlsoup.SQLSoup(cs)
db.schema = "lbs2"