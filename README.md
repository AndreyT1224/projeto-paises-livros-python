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
