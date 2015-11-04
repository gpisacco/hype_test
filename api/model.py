import sqlsoup
import os
import ConfigParser
import io


config = ConfigParser.RawConfigParser(allow_no_value=True)
inif = open(os.environ['CONFIG'],'rb')
config.readfp(inif)


PG_USER = config.get('hype', 'PG_USER')
PG_PASS = config.get('hype','PG_PASSWORD')
PG_HOST = config.get('hype','PG_HOST')
PG_DBNAME = config.get('hype','PG_DBNAME')

#connection template
ct = "postgresql://{}:{}@{}/{}"

#connection string 
cs = ct.format(PG_USER,PG_PASS,PG_HOST,PG_DBNAME)
db  = sqlsoup.SQLSoup(cs)
db.schema = "lbs2"