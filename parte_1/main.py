import sqlite3 as sql
from fastapi import FastAPI
import uvicorn

# Rodar API - uvicorn main:app
# http://127.0.0.1:8000/doc
# http://127.0.0.1:8000/redoc

# Cliente thunder raio

banco = "cart.db"

# Comandos SQL
contagem = "SELECT COUNT(*) FROM Carrinho;"
criar_table = "CREATE TABLE IF NOT EXISTS Carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL);"
select_todos = "SELECT * FROM Carrinho;"
truncate = "DELETE FROM Carrinho;" #"TRUNCATE TABLE carrinho;"
select_id = "SELECT * FROM Carrinho WHERE id_prod like ?;"
delete_id = "DELETE FROM Carrinho WHERE id_prod = ?;"
inserir_prod = "INSERT INTO Carrinho VALUES (:id,:Nome,:Preco,:Quantidade,:Descrição,);"
atualiza_prod = "UPDATE carrinho SET quantidade = [valor] WHERE id_prod = [id_produto];" 

def abrir_conexao(banco):
    conn = sql.connect(banco) #connection to db
    cursor = conn.cursor() #create a cursor
    return conn, cursor

def fechar_conexao(conn):
    conn.commit()
    conn.close()

app= FastAPI()

@app.get('/') # FUNCIONANDO
async def criar_tabela(): 
    return ("SEJA BEM VINDO(A) A API ORGANICOS ")

@app.post('/criar_tabela') # FUNCIONADO
async def criar_tabela(): 
    conn, cursor = abrir_conexao(banco)
    resutado = cursor.execute(criar_table)
    print(resutado)
    fechar_conexao(conn)
    return("Cadastrado, vide console.")

@app.get('/consulta') # FUNCIONANDO
def consulta_tabela():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.put('/modifica') # testando - ERROR 500
def modificar_prod(id_produto, valor):
    conn, cursor = abrir_conexao(banco) # abertura do banco
    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE [condition];
    resultado = cursor.execute(atualiza_prod)
    print(resultado)
    fechar_conexao(conn)
    return {'Produto cadastrado: ': f'{resultado}'}

@app.delete('/deleta') # FUNCIONANDO
def deleta_tabela():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Carrinho apagado!'}

# uvicorn main:app