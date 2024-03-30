import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    dsn = oracledb.makedsn(host, port, service_name='orcl')
    return oracledb.connect(user=user, password=password, dsn=dsn)