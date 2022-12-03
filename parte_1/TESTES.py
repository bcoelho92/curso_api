'''
* Adição de produtos -
* Remoção de produtos - 
* Alteração de quantidade -
* Consulta de itens - 
'''
import sqlite3 as sql
from flask import Flask, redirect, url_for, request, render_template 
from json import dumps

banco = "cart.db"

# Comandos SQL
contagem = "SELECT COUNT(*) FROM Carrinho;"
criar_table = "CREATE TABLE IF NOT EXISTS Carrinho (id_prod INTEGER PRIMARY KEY, Nome TEXT NOT NULL, Preço REAL NOT NULL, Quantidade INTEGER NOT NULL, Descrição TEXT NOT NULL);"
select_todos = "SELECT * FROM Carrinho;"
truncate = "DELETE FROM Carrinho;" #"TRUNCATE TABLE carrinho;"
select_id = "SELECT * FROM Carrinho WHERE id_prod like ?;"
delete_id = "DELETE FROM Carrinho WHERE id_prod = ?;"
inserir_prod = "INSERT INTO Carrinho VALUES (:id,:Nome,:Preco,:Quantidade,:Descrição,);"
atualiza_prod = "UPDATE carrinho SET quantidade = [valor] WHERE id_prod = [id_produ];" 

app = Flask(__name__)

#----- topico 3. carrinho 

def abrir_conexao(banco):
    conn = sql.connect(banco) #connection to db
    cursor = conn.cursor() #create a cursor
    return conn, cursor

def fechar_conexao(conn):
    conn.commit()
    conn.close()

# ROTAS

@app.route('/')
def main():
    return render_template("index.html") 

@app.route('/criar_tabela', methods=['POST']) # testando - ok
def criar_table():
    conn, cursor = abrir_conexao(banco)
    resutado = cursor.execute(criar_table)
    print(resutado)
    fechar_conexao(conn)
    return("Cadastrado, vide console.")
    
# @app.route('/adc_m/', methods=['PUT']) # ADICONAR VARIOS ITENS - adicionar form
# def inser_vprod():
#     conn, cursor = abrir_conexao(banco)
#     data = [
#        (1,'Cacau',12.5,3,'Do Brasil'),
#        (2,'Arroz',10,2,'Do Brasil'),
#     ]
#     cursor.executemany('INSERT INTO carrinho VALUES(?,?,?,?,?)', data)
#     resultado = cursor.execute(select_todos)
#     print(resultado)
#     fechar_conexao(conn)
#     return("Cadastrado, vide console.")

@app.route('/cadastro', methods=['POST']) # ADICIONAR 1 ITEM - adicionar form
def inser_prod():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    cursor.execute(inser_prod)
    conn.commit()
    fechar_conexao(conn)
    print(banco)
    return("Cadastrado, vide console.")

@app.route('/modifica/<id_produ>/<valor>', methods=['PUT']) # testando - 
def modificar_prod(id_produ, valor):
    conn, cursor = abrir_conexao(banco) # abertura do banco
    # UPDATE table_name SET column1 = value1, column2 = value2 WHERE [condition];
    resultado = cursor.execute(atualiza_prod)
    print(resultado)
    fechar_conexao(conn)
    return {'Produto cadastrado: ': f'{resultado}'}

@app.route('/consulta', methods=['POST']) # CONULTAR TABLE POR ID_PROD - OK
def consulta_t():
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_todos).fetchall() 
    print(resultado)
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.route('/consulta/<int:id_produto>', methods=['GET']) # CONULTAR TABLE POR ID_PROD - OK
def consulta_id(id_produto):
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(select_id).fetchall() 
    print(resultado)
    fechar_conexao(conn)
    return {'Produtos': f'{resultado}'}

@app.route('/produtos', methods=['GET']) # CONTAGEM DE PRODUTOS - OK
def prod_cont():    
    conexao, cursor = abrir_conexao(banco)
    resultado = cursor.execute(contagem).fetchone()
    print(resultado)
    fechar_conexao(conexao)
    return {'Produtos': f'{resultado[0]} Itens no carrinho'}

@app.route('/deleta/<int:id_produto>', methods=['DELETE']) # testar
def remover_prod(id_produto):
    conn, cursor = abrir_conexao(banco) # abertura do banco
    resultado = cursor.execute(delete_id)
    print(resultado)
    fechar_conexao(conn) # fecha o banco
    return {'Produtos': f'{resultado} Deletado'}

@app.route('/deleta')
def deleta_tudo():
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(truncate)
    fechar_conexao(conexao)
    return {'message': 'Carrinho apagado!'}
    
if __name__ == "__main__":
    app.run(debug=True)