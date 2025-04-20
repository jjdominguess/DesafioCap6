from datetime import datetime
import DBAction as actions
import Utils
import pandas
import jsonConverter

# criação da lista
insumos = []

# Cadastra novo insumo
def cadastrar_insumo():
    print()
    nome = input("Nome do insumo: ")
    tipo = input("Tipo (semente, fertilizante, defensivo): ")
    quantidade = int(input("Quantidade (unidades): "))
    validade = input("Data de validade (dd/mm/aaaa): ")
    custo = float(input("Custo por unidade (R$): "))
    
    print("Cadastrando insumo...")
    
    insumo = {
        "nome": nome,
        "tipo": tipo,
        "quantidade": quantidade,
        "validade": validade,
        "custo": custo
    }
    insumos.append(insumo)
    
    actions.cadastrarInsumo(nome=nome, tipo=tipo, quantidade=quantidade, validade=validade, custo=custo)
    print("Insumo cadastrado com sucesso!")

# Lista todos os insumos
def listar_insumos():
    print()
    lista = actions.listarInsumos()
    if lista == []:
        print("Não há insumos cadastrados!")
    else:
        tratamentoInfoDataFrame = pandas.DataFrame.from_records(lista,columns=['id','nome','tipo','quantidade','validade','custo'], index='nome')
        print(tratamentoInfoDataFrame)
        
    print("\nLISTADOS!")
  
# Busca insumo por nome
def buscar_insumo():
    print()
    termo = input("Digite o nome para buscar: ") #.lower()
    actions.buscarInsumo(termo)

# Editar insomos
def editar_insumo():
    print()
    try:
        # Solicita o ID do insumo a ser editado
        idInsumo = int(input("Qual o ID do insumo que deseja alterar? "))
        
        # Verifica se o ID existe no banco de dados
        consultaID = actions.consultaIdInsumo(idInsumo)
        if not consultaID:
            print(f"Insumo com ID {idInsumo} não encontrado.")
            return

        # Solicita novos valores para os campos
        print("Pressione Enter para manter o valor atual.")
        novo_nome = input("Novo nome: ")
        novo_tipo = input("Novo tipo: ")
        nova_qtd = input("Nova quantidade: ")
        nova_validade = input("Nova validade (dd/mm/aaaa): ")
        novo_custo = input("Novo custo: ")

        # Valida e mantém os valores antigos se o usuário não inserir nada
        if nova_qtd:
            try:
                nova_qtd = int(nova_qtd)
            except ValueError:
                print("Quantidade inválida. Deve ser um número inteiro.")
                return

        if novo_custo:
            try:
                novo_custo = float(novo_custo)
            except ValueError:
                print("Custo inválido. Deve ser um número.")
                return

        # Valida o formato da data
        if nova_validade:
            try:
                # Converte a data para o formato correto
                datetime.strptime(nova_validade, "%d/%m/%Y")
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")
                return
        
        # Chama a função para editar o insumo no banco de dados
        actions.editarInsumo(
            id=idInsumo,
            novoNome=novo_nome or None,
            novoTipo=novo_tipo or None,
            novaQuantidade=nova_qtd or None,
            novaValidade=nova_validade or None,
            novoCusto=novo_custo or None
        )
        print("Insumo atualizado com sucesso.")   
    except ValueError:
        print("Entrada inválida. Use apenas números para o ID.")
    except Exception as e:
        print(f"Erro ao editar insumo: {e}")
    finally:
        Utils.waitAndClean(5)    

# Exclui um insumo
def excluir_insumo():
    print()
    listar_insumos()
    nuneroInsumoTabela = actions.contarItensTabela()
            
    if not nuneroInsumoTabela:
        # TODO: Testar ausência de insumos na tabela.
        print("Não existem insumos cadastrados.")
        return

    try:
        indice = int(input("Digite o número do insumo que deseja excluir: "))
        if indice <= 0 or indice > nuneroInsumoTabela:
            print("Digite um número válido!")
            return
        else: 
            actions.exclusaoInsumo(id=indice)
    except actions.oracledb.DatabaseError as e:
        error, = e.args
        print(f"Erro {e} na tentativa de exclusão do insumo.")

# Verifica insumos vencidos
def verificar_insumos_vencidos():
    print()
    vencidos = actions.consultaValidadeInsumo()
    print(vencidos)

def passar_tabela_json():
    lista = actions.listarInsumosComoDicionario()
    
    jsonConverter.convertJson(lista)
    print(lista)

# Menu principal
def menu():
    while True:
        print("\n--- Controle de Insumos Agrícolas ---")
        print("1. Cadastrar insumo")
        print("2. Listar insumos")
        print("3. Buscar insumo por nome")
        print("4. Editar insumo")
        print("5. Excluir insumo")
        print("6. Verificar insumos vencidos")
        print("7. Exportar dados de insumos para JSON")
        print("8. Salvar e sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_insumo()
        elif opcao == "2":
            listar_insumos()
        elif opcao == "3":
            buscar_insumo()
        elif opcao == "4":
            editar_insumo()
        elif opcao == "5":
            excluir_insumo()
        elif opcao == "6":
            verificar_insumos_vencidos()
        elif opcao == "7":
            passar_tabela_json()
        elif opcao == "8":
            print("Até a próxima.")
        else:
            print("Opção inválida. Tente novamente.")

# Início da aplicação
if __name__ == "__main__":
    menu()
