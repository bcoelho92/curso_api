** Criar ambiente **
python3 -m venv env

** Ativar ambiente **
source env/bin/activate

** foto dos requisitos **
python -m pip freeze 

python -m pip install 

** adicionar requerimentos em um arquivo **
python -m pip freeze > requirements.txt 

** ler o arquivo de requisição ** 
cat requirements.txt

** instalar os requisitos do arquivo **
python -m pip install -r requirements.txt

** RODAR API para atualizar automaticamente

pip install uvicorn 
uvicorn main:app -- reload

if __name__ == '__main__':
    import uvicorn

    uvicorn.rum("main:app", host="127.0.0.1", port=8000,log_level="info", reload=True )
    
# rodar API direto com Python - python main.py

** Execução no começo do deploy
pip install gunicorn 

gunicorn main:app -w 4 -k uvicorn.workers.uvicornworker 

-w 4 = numero de servidores 
-k = qualq classe para executar (Uvicorn de alto desempenho)

