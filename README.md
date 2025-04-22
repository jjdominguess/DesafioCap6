# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

# Nome do projeto
  Python e além: Gestão de agronegócio
## 👨‍🎓 Integrantes: 
- <a>João José Domingues Silva</a>
- <a>Lais Londo Claus</a>
- <a>Murilo Santana</a> 
- <a>Lucas Alves Ladeira</a> 
- <a>Carlos Eduardo Campos Lanzi</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>

## 📜 Descrição

*Este projeto é uma aplicação para gerenciar insumos agrícolas, permitindo o cadastro, consulta, edição, exclusão e exportação de dados para JSON. Ele utiliza um banco de dados Oracle para armazenar as informações e oferece uma interface de menu interativo para o usuário.*

  
## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>DB_Service</b>: Esta pasta possui o arquivo responsável por estabelecer a conexão com o banco de dados Oracle e criar a tabela de insumos, caso ela ainda não exista.

- <b>Utils</b>: Esta pasta possui o arquivo responsável por funções utilitárias para limpar a tela e pausar a execução do programa.

- <b>DBAction</b>: Esta pasta contém o arquivo responsável por funções principais para manipulação dos dados no banco de dados. Ele utiliza a conexão estabelecida em `DBIntegration.py` e fornece funcionalidades como cadastro, consulta, edição e exclusão de insumos.

- <b>MenuFarmIntegrateDB.py</b>: Este arquivo implementa o menu principal da aplicação, permitindo que o usuário interaja com as funcionalidades do sistema.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

* Primeiro é necessário preencher os campos "user" e "password" com um usuário e senha valida no Oracle DB ![image](https://github.com/user-attachments/assets/ef6ed51d-308d-400f-b35c-d73935f68ae9)
  após isso, utilizando o comando no terminal "python MenuFarmIntegrateDB.py" no local onde se encontra o arquivo(python MenuFarmIntegrateDB.py).*



## 🗃 Histórico de lançamentos

* 1.0.0 - 21/04/2025

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
