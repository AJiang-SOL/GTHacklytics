import os
from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import sqlalchemy

# # initialize Connector object
# connector = Connector()

# # function to return the database connection
# def getconn() -> pymysql.connections.Connection:
#     conn: pymysql.connections.Connection = connector.connect(
#         "hackgt-377513:us-central1:hackgt",
#         "pymysql",
#         user="ajiang",
#         password="1234",
#         db="NuTree"
#     )
#     return conn

# def pool():
#     pool = sqlalchemy.create_engine(
#     "mysql+pymysql://",
#     creator=getconn,
# )
#     return pool.connect()

# pool()
def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of SQL Server.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"] = "hackgt-377513:us-central1:hackgt"   # e.g. 'project:region:instance'
    db_user = os.environ.get("DB_USER", "")  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"] = "1234" # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"] = "NuTree"  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    connector = Connector(ip_type)

    connect_args = {}
    # If your SQL Server instance requires SSL, you need to download the CA
    # certificate for your instance and include cafile={path to downloaded
    # certificate} and validate_host=False. This is a workaround for a known issue.
    if os.environ.get("DB_ROOT_CERT"):  # e.g. '/path/to/my/server-ca.pem'
        connect_args = {
            "cafile" : os.environ["DB_ROOT_CERT"],
            "validate_host": False,
        }

    def getconn():
        conn = connector.connect(
            instance_connection_name,
            "pytds",
            user=db_user,
            password=db_pass,
            db=db_name,
            **connect_args
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mssql+pytds://localhost",
        creator=getconn,
        # ...
    )
    return pool
connect_with_connector()



