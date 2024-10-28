# 📝 Gerenciador de Tarefas

## 📖 Introdução  
O **Gerenciador de Tarefas** é uma aplicação web simples desenvolvida em Python usando o framework Flask. O objetivo principal do projeto é permitir que usuários criem, editem, e gerenciem suas tarefas diárias de forma eficiente. 

Esta aplicação inclui funcionalidades básicas como **login/cadastro de usuários**, criação de tarefas com **data de vencimento**, **marcação de status** (completa/incompleta), e **edição ou exclusão** de tarefas. 

O projeto foi construído pensando em boas práticas de desenvolvimento com Flask, PostgreSQL e autenticação de usuários, ideal para quem quer entender como desenvolver uma aplicação web com backend robusto e login seguro.

---

## 🎯 Funcionalidades
- **Login e Cadastro de Usuário:** Controle de acesso para garantir que cada usuário veja apenas suas tarefas.
- **Dashboard de Tarefas:** Exibe todas as tarefas criadas pelo usuário.
- **Criação de Tarefas:** Permite definir título, descrição e data de vencimento para cada tarefa.
- **Edição e Exclusão de Tarefas:** O usuário pode alterar ou remover tarefas.
- **Marcação de Status:** Define uma tarefa como “completa” ou “incompleta” com um clique.

---

## 🚀 Relevância do Projeto
Este projeto é uma ótima introdução ao desenvolvimento de aplicações web em Python com Flask e PostgreSQL. Ele aborda conceitos como:
- **Autenticação de usuários** com sessões.
- **Interação com banco de dados relacional** (PostgreSQL).
- **Arquitetura modular** com rotas e modelos organizados.
- **Renderização de templates dinâmicos** usando Jinja.

É uma base sólida que pode ser expandida para projetos maiores ou adaptada para outras áreas, como listas de compras, aplicativos de produtividade, ou sistemas de gerenciamento de clientes.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Flask 3.x**
- **SQLAlchemy 2.x** 
- **PostgreSQL** para banco de dados.
- **Bootstrap 5.3** para estilização.
- **HTML/CSS** para templates e customizações.

---

## ⚙️ Como Configurar o Projeto Localmente

### Pré-requisitos
- **Python 3.x** instalado.
- **PostgreSQL** instalado e configurado.
- Ferramenta para gerenciar ambientes virtuais (`venv` ou `virtualenv`).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Robert-Cortez-Rudi/Gerenciamento_Tarefas.git
   cd Gerenciamento_Tarefas

2. **Crie e ative um ambiente virtual:**

   - No Windows:
     ```python
     python -m venv .venv
     .venv\Scripts\activate
    
   - No Linux/Mac:
   ```bash
   python -m venv .venv
   source .venv/bin/activate


3. **Instalar as dependências**

   ```python
   pip install -r requirements.txt


4. **Configurar/Defina as variaveis de ambiente**

   São utilizadas três variaves de ambiente para melhorar a segurança e facilitar a configuração do projeto. 

   Crie um arquivo .env e insira as seguintes configurações com seus dados:

   ```python
   SECRET_KEY = "Sua chave secreta"
   DATABASE_URL = "postgresql://usuario:senha@localhost/seu_banco"
   WTF_CSRF_SECRET_KEY = "sua_chave_csrf_secreta"

5. **Executar o servidor**

   ```python
   python .\app.py


   
