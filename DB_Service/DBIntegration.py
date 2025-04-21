import os
import time
import oracledb
import Utils.Utils as Utils

flagConexao: bool

# ========================== ESTABELECE CONEXÃO COM O BANCO DE DADOS ==========================

def conexaoDB():
    try:
        conexao = oracledb.connect(
            user="",
            password="",
            dsn="oracle.fiap.com.br:1521/ORCL",
        )
    except oracledb.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        flagConexao == False
        return False
    else:
        print("Conexão estabelecida com sucesso.")
        flagConexao = True
        return conexao

# ========================== CRIAÇÃO DA TABELA INSUMOS ==========================
def tabelaInsumos():
    conexao = conexaoDB()
    if not conexao:
        return
    try:
        cursor = conexao.cursor()
    
        cursor.execute("""
            select count(*) 
            from user_tables 
            where table_name = 'INSUMOS'
        """)
        if  cursor.fetchone()[0] > 0:
            print("Tabela já existe.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        else:
            cursor.execute("""
                create table INSUMOS (
                    id number generated always as identity primary key,
                    nome varchar2(30),
                    tipo varchar2(30),
                    quantidade float,
                    validade date,
                    custo float
                )
            """)
            print("Tabela criada com sucesso.")
            conexao.commit()
            Utils.waitAndClean(3)
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao criar tabela: Código {error.code}, Mensagem: {error.message}")


