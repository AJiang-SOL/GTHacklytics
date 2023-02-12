import os

from google.cloud.sql.connector import Connector, IPTypes
import pymysql

import sqlalchemy

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "hackgt-377513:us-central1:hackgt",
        "pymysql",
        user="alexj",
        password="12345",
        db="BasicFood"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
