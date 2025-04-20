# Controle de Insumos Agrícolas

Este projeto é uma aplicação para gerenciar insumos agrícolas, permitindo o cadastro, consulta, edição, exclusão e exportação de dados para JSON. Ele utiliza um banco de dados Oracle para armazenar as informações e oferece uma interface de menu interativo para o usuário.

---

## Estrutura do Projeto

A estrutura do projeto é composta pelos seguintes arquivos:

### Arquivos e Suas Funções

#### **1. `DBAction.py`**
Este arquivo contém as funções principais para manipulação dos dados no banco de dados. Ele utiliza a conexão estabelecida em `DBIntegration.py` e fornece funcionalidades como cadastro, consulta, edição e exclusão de insumos.

- **Funções Implementadas:**
  - `cadastrarInsumo(nome, tipo, quantidade, validade, custo)`: Insere um novo insumo no banco de dados.
  - `listarInsumos() -> list`: Retorna todos os insumos cadastrados no banco de dados como uma lista.
  - `listarInsumosComoDicionario() -> list`: Retorna os insumos como uma lista de dicionários.
  - `buscarInsumo(nome)`: Busca insumos pelo nome, ignorando maiúsculas/minúsculas e acentos.
  - `contarItensTabela() -> int`: Retorna o número total de insumos cadastrados.
  - `consultaIdInsumo(id) -> bool`: Verifica se um insumo com o ID fornecido existe.
  - `consultaValidadeInsumo() -> list`: Retorna os insumos cuja validade já expirou.
  - `editarInsumo(id, novoNome, novoTipo, novaQuantidade, novaValidade, novoCusto)`: Atualiza os dados de um insumo com base no ID.
  - `excluirTabela()`: Exclui a tabela de insumos do banco de dados.
  - `exclusaoInsumo(id)`: Exclui um insumo específico com base no ID.

---

#### **2. `DBIntegration.py`**
Este arquivo é responsável por estabelecer a conexão com o banco de dados Oracle e criar a tabela de insumos, caso ela ainda não exista.

- **Funções Implementadas:**
  - `conexaoDB()`: Estabelece a conexão com o banco de dados Oracle.
  - `tabelaInsumos()`: Cria a tabela `INSUMOS` no banco de dados, caso ela ainda não exista.

---

#### **3. `MenuFarmIntegrateDB.py`**
Este arquivo implementa o menu principal da aplicação, permitindo que o usuário interaja com as funcionalidades do sistema.

- **Funções Implementadas:**
  - `cadastrar_insumo()`: Permite ao usuário cadastrar um novo insumo.
  - `listar_insumos()`: Lista todos os insumos cadastrados.
  - `buscar_insumo()`: Permite ao usuário buscar um insumo pelo nome.
  - `editar_insumo()`: Permite ao usuário editar os dados de um insumo existente.
  - `excluir_insumo()`: Permite ao usuário excluir um insumo pelo ID.
  - `verificar_insumos_vencidos()`: Lista os insumos cuja validade já expirou.
  - `passar_tabela_json()`: Exporta os dados dos insumos para um arquivo JSON.
  - `menu()`: Exibe o menu principal e gerencia a navegação entre as opções.

---

#### **4. `jsonConverter.py`**
Este arquivo é responsável por converter os dados dos insumos para o formato JSON e salvá-los em um arquivo.

- **Funções Implementadas:**
  - `convertJson(lista)`: Converte uma lista de insumos para JSON, tratando valores do tipo `Timestamp`, e salva o resultado no arquivo `Insumos.json`.

---

#### **5. `Utils.py`**
Este arquivo contém funções utilitárias para limpar a tela e pausar a execução do programa.

- **Funções Implementadas:**
  - `waitAndClean(seconds)`: Aguarda um número de segundos e limpa a tela do terminal.

---

#### **6. `Insumos.json`**
Este arquivo armazena os dados dos insumos exportados no formato JSON. Ele é gerado pela função `convertJson` do arquivo `jsonConverter.py`.

---

## Fluxo de Execução

1. **Início da Aplicação:**
   - O programa começa com a execução do arquivo `MenuFarmIntegrateDB.py`, que exibe o menu principal.

2. **Interação com o Usuário:**
   - O usuário pode escolher entre as opções do menu para cadastrar, listar, buscar, editar, excluir ou exportar insumos.

3. **Manipulação de Dados:**
   - As funções em `DBAction.py` são chamadas para realizar operações no banco de dados.

4. **Exportação para JSON:**
   - Os dados podem ser exportados para o arquivo `Insumos.json` usando a opção correspondente no menu.

---

## Requisitos

- **Linguagem:** Python 3.10 ou superior.
- **Bibliotecas Necessárias:**
  - `oracledb`
  - `pandas`
  - `json`
  - `os`
  - `time`
- **Banco de Dados:** Oracle Database.

---

## Como Executar

1. Certifique-se de que o banco de dados Oracle está configurado e acessível.
2. Instale as dependências necessárias:
   ```bash
   pip install oracledb pandas