📘 Projeto: Coleta de Dados de Países e Livros com Python
🔍 Descrição
Este projeto automatiza a extração de dados públicos sobre países e livros, armazenando essas informações em bancos SQLite e gerando um relatório final em Excel. Foi desenvolvido como parte de uma atividade avaliativa da disciplina de RPA.

🧠 Funcionalidades
🔹 Parte 1 – API REST
Solicita o nome de 3 países ao usuário

Extrai dados da API REST Countries

Armazena os dados em paises.db

🔹 Parte 2 – Web Scraping
Coleta os 10 primeiros livros do site Books to Scrape

Extrai título, preço, avaliação e disponibilidade

Armazena os dados em livraria.db

🔹 Parte 3 – Relatório
Gera um relatório final em Excel (relatorio_final.xlsx)

Contém os dados dos países e livros, nome do autor e data

⚙️ Tecnologias utilizadas
Python 3.x

requests

BeautifulSoup

openpyxl

sqlite3 (embutido no Python)

🚀 Como executar o projeto
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/projeto-paises-livros-python.git
cd projeto-paises-livros-python
Instale as dependências (se ainda não tiver):

bash
Copiar
Editar
pip install requests beautifulsoup4 openpyxl
Execute o script:

bash
Copiar
Editar
python projeto_final.py
Digite o nome de 3 países quando solicitado.

Os arquivos paises.db, livraria.db e relatorio_final.xlsx serão gerados automaticamente.

👤 Autor
Nome: 
Andrey Tomaz   RA: 2400729
Henry Modesto  RA: 2401244
Data de entrega: 30/05/2025


