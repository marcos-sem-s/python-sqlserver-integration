from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

Base = declarative_base()
load_dotenv()

class User(Base):
    __tablename__ = 'produtos'
    
    codigo_produto = Column(String, primary_key=True)
    nome_produto = Column(String)
    embalagem = Column(String)
    tamanho = Column(String)
    sabor = Column(String)
    preco_lista = Column(Float)

connection_string = (
    f"mssql+pyodbc://{os.getenv('UID')}:{os.getenv('PWD')}@\
        {os.getenv('SERVER')}/{os.getenv('DATABASE')}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = User(
    codigo_produto='2422798', 
    nome_produto='Vinho grosso',
    embalagem='Vidro',
    tamanho='770 ml',
    sabor='Uva',
    preco_lista='50.5'
)
session.add(novo_usuario)

session.commit()
