import DB_Service.DBIntegration as db
import pandas
import oracledb
import Utils.Utils as Utils

conexao = db.conexaoDB()
cursor = conexao.cursor()
nomeN = "Nitrato"
# ========================== CADASTRO DE INSUMO ==========================

def cadastrarInsumo(nome, tipo, quantidade, validade, custo):
    
    try:
        cadastroInsumo = f"""
            INSERT INTO INSUMOS (nome, tipo, quantidade, validade, custo)
            VALUES (:nome, :tipo, :quantidade, TO_DATE(:validade, 'DD/MM/YYYY'), :custo)
        """
        cursor.execute(cadastroInsumo, { 
            "nome": nome,
            "tipo": tipo,
            "quantidade": quantidade,
            "validade": validade,
            "custo": custo
        })
    except oracledb.DatabaseError as e:
        print("Erro ao cadastrar insumo.", e)
    finally:
        conexao.commit()

# ========================== CONSULTA DE INSUMOS ==========================

def listarInsumos()-> list:
    listaInsumos = []
    
    consultaInsumos = f"""
        SELECT * FROM INSUMOS
        """
    cursor.execute(consultaInsumos)
    data = cursor.fetchall()
    
    for dt in data:
        listaInsumos.append(dt)
    
    listaInsumos = sorted(listaInsumos)
    return listaInsumos

def listarInsumosComoDicionario() -> list:
    try:
        consultaInsumos = "SELECT * FROM INSUMOS"
        cursor.execute(consultaInsumos)
        data = cursor.fetchall()

        # Converte os resultados para um DataFrame
        colunas = [col[0] for col in cursor.description]  # Obtém os nomes das colunas
        insumos_df = pandas.DataFrame(data, columns=colunas)

        # Converte o DataFrame para uma lista de dicionários
        lista_insumos = insumos_df.to_dict(orient="records")
        return lista_insumos
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao listar insumos: Código {error.code}, Mensagem: {error.message}")
        return []

def buscarInsumo(nome):
    listaInsumosEspecificos = []
    try:   
        # Normaliza o nome para ignorar maiúsculas/minúsculas e acentos
        consultaInsumo = """
            SELECT * FROM INSUMOS
            WHERE UPPER(TRANSLATE(nome, 
                'ÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇÑáéíóúàèìòùâêîôûãõçñ', 
                'AEIOUAEIOUAEIOUAOCNAEIOUAEIOUAEIOUAOCN')) = 
                UPPER(TRANSLATE(:nome, 
                'ÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇÑáéíóúàèìòùâêîôûãõçñ', 
                'AEIOUAEIOUAEIOUAOCNAEIOUAEIOUAEIOUAOCN'))
            """
        cursor.execute(consultaInsumo, {"nome": nome})
        data = cursor.fetchall()
        
        if not data: 
            print(f"Não há insumo(s) cadastrado(s) com o nome{nome}")
        else:      
            for dt in data:
                listaInsumosEspecificos.append(dt)
        
        tratamentoInfoDataFrame = pandas.DataFrame.from_records(listaInsumosEspecificos,columns=['id','nome','tipo','quantidade','validade','custo'], index='nome')
    except:
        print("Erro na transação do bando de dados")
    else:
        Utils.waitAndClean(3)
        print(f"Informações achadas do insumo {nome}:  \n{tratamentoInfoDataFrame}")
        
def contarItensTabela() -> int:
    try:
        consulta = "SELECT COUNT(*) FROM INSUMOS"
        cursor.execute(consulta)
        total = cursor.fetchone()[0]  # Retorna o número total de registros
        print(total)
        return total
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao contar itens na tabela: Código {error.code}, Mensagem: {error.message}")
        return 0

def consultaIdInsumo(id) -> bool:
    try:
        consultaID = f""" SELECT * FROM INSUMOS WHERE ID= :id """
        cursor.execute(consultaID, {"id":id})
        data = cursor.fetchone()
        
        if data:
            return True
        else:
            return False
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao consultar insumo pelo ID: Código {error.code}, Mensagem: {error.message}")
        return False
    
def consultaValidadeInsumo() -> list:
    try:
        # Consulta SQL para buscar insumos com validade anterior à data atual
        consultaValidade = """SELECT * FROM INSUMOS WHERE validade < SYSDATE"""
        cursor.execute(consultaValidade)
        data = cursor.fetchall()
        
        tratamentoData = pandas.DataFrame.from_records(data, columns=['id','nome','tipo','quantidade','validade','custo'], index='validade')
        
        if data:
            return tratamentoData  # Retorna os insumos vencidos
        else:
            # print("Nenhum insumo vencido encontrado.")
            return []
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao consultar validade dos insumos: Código {error.code}, Mensagem: {error.message}")
        return []
    
# ========================== EDIÇÃO DE DADOS ==========================

def editarInsumo(id, novoNome=None, novoTipo=None, novaQuantidade=None, novaValidade=None, novoCusto=None):
    try:
        # Monta a consulta SQL dinamicamente
        campos = []
        valores = {"id": id}

        if novoNome is not None:
            campos.append("nome = :nome")
            valores["nome"] = novoNome
        if novoTipo is not None:
            campos.append("tipo = :tipo")
            valores["tipo"] = novoTipo
        if novaQuantidade is not None:
            campos.append("quantidade = :quantidade")
            valores["quantidade"] = novaQuantidade
        if novaValidade is not None:
            campos.append("validade = TO_DATE(:validade, 'DD/MM/YYYY')")
            valores["validade"] = novaValidade
        if novoCusto is not None:
            campos.append("custo = :custo")
            valores["custo"] = novoCusto

        # Verifica se há campos para atualizar
        if not campos:
            print("Nenhum campo para atualizar.")
            return

        # Junta os campos para a consulta SQL
        campos_sql = ", ".join(campos)
        consulta = f"UPDATE INSUMOS SET {campos_sql} WHERE id = :id"

        # Executa a consulta
        cursor.execute(consulta, valores)
        conexao.commit()
        
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao editar insumo: Código {error.code}, Mensagem: {error.message}")

# ========================== EXCLUSÃO DA TABELA OU CAMPOS DA TABELA ==========================

def excluirTabela():    
    try:
        cursor = conexao.cursor()
        cursor.execute("DROP TABLE INSUMOS")
        print("Tabela excluída com sucesso.")
        conexao.commit()
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao excluir tabela: Código {error.code}, Mensagem: {error.message}")
    finally:
        cursor.close()
        conexao.close()

def exclusaoInsumo(id):
    try: 
        consulta = "DELETE FROM INSUMOS WHERE ID = :id"
        cursor.execute(consulta, {"id": id})
        conexao.commit()
        print(f"Insumo com ID {id} excluído com excluído com sucesso.")
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro ao excluir insumo: Código {error.code}, Mensagem: {error.message}")
