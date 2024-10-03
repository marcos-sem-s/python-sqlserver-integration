import os
from dotenv import load_dotenv

import pyodbc

load_dotenv()

conn = (
    "Driver={SQL SERVER};"
    f"Server={os.getenv('SERVER')};"
    "Database=suco_vendas;"
    f"UID={os.getenv('UID')};"
    f"PWD={os.getenv('PWD')};"
)

conn = pyodbc.connect(conn)
cursor = conn.cursor()

print('Conexão bem sucedida')
