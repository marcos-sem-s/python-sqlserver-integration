from dotenv import load_dotenv
import pyodbc

import os

load_dotenv()

conn = (
    "Driver={SQL SERVER};"
    f"Server={os.getenv('SERVER')};"
    f"Database={os.getenv('DATABASE')};"
    f"UID={os.getenv('UID')};"
    f"PWD={os.getenv('PWD')};"
)

conn = pyodbc.connect(conn)
cursor = conn.cursor()

print('Conexão bem sucedida')

query = """
INSERT INTO produtos (
    codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_lista
)
VALUES (
    '1122767', 'Vinho tinto', 'Vidro', '700 ml', 'Uva', 33.5
);
"""

cursor.execute(query)
cursor.commit()
print('Query feita')
