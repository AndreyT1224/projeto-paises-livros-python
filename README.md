<h1 align="center">📘 Coleta de Dados de Países e Livros com Python</h1>

<p align="center">
  Projeto desenvolvido para automatizar a extração de dados públicos de países e livros, utilizando técnicas de API REST, Web Scraping e geração de relatórios em Excel.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/SQLite-integrado-lightgrey?logo=sqlite" />
  <img src="https://img.shields.io/badge/BeautifulSoup-web--scraping-yellow?logo=beautifulsoup" />
  <img src="https://img.shields.io/badge/openpyxl-relatório-brightgreen?logo=excel" />
</p>

---

## 🎯 Objetivo

Automatizar a coleta de dados públicos a partir de uma API e de um site, armazenando as informações em bancos de dados locais e gerando um relatório consolidado em Excel. O projeto é dividido em três partes:

---

## 🧠 Funcionalidades

### 🔹 Parte 1 – API REST
- Solicita ao usuário o nome de **3 países**
- Extrai dados da **API REST Countries**
- Armazena os dados em `paises.db`

### 🔹 Parte 2 – Web Scraping
- Acessa o site **Books to Scrape**
- Coleta os **10 primeiros livros**
- Extrai:
  - Título
  - Preço
  - Avaliação
  - Disponibilidade
- Armazena os dados em `livraria.db`

### 🔹 Parte 3 – Relatório
- Gera um arquivo Excel `relatorio_final.xlsx`
- Inclui:
  - Dados dos países
  - Dados dos livros
  - Nome dos autores e data de execução

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **requests**
- **BeautifulSoup4**
- **openpyxl**
- **sqlite3** (embutido no Python)

---

## 💻 Como Executar o Projeto

<details>
<summary><strong>📂 Acesse a pasta do projeto via terminal</strong></summary>

```bash
cd projeto-paises-livros-python
```
</details>

<details>
<summary><strong>🔧 Instale as dependências</strong></summary>

```bash
pip install requests beautifulsoup4 openpyxl
```
</details>

<details>
<summary><strong>🚀 Execute o script</strong></summary>

```bash
python projeto_final.py
```

Digite o nome de 3 países quando solicitado.  
Os arquivos `paises.db`, `livraria.db` e `relatorio_final.xlsx` serão gerados automaticamente.
</details>

---

## 👨‍💻 EQUIPE DE DESENVOLVIMENTO

<table align="center">
  <tr>
    <td align="center" style="padding: 10px;">
      <a href="https://github.com/HenryModesto" title="Github Henry" style="text-decoration: none; color: black;">
        <img src="./pictures/Henry.jpeg" width="200px" height="200px" alt="Foto de Henry Oliveira Modesto De Jesus" style="border-radius: 8px;"/><br>
        <sub>
          <b>HENRY MODESTO</b><br>
          <b>RA: 2401244</b>
        </sub>
      </a>
    </td>
    <td align="center" style="padding: 10px;">
      <a href="https://github.com/AndreyT1224" title="Github Andrey" style="text-decoration: none; color: black;">
        <img src="./pictures/Andrey.jpeg" width="190px" alt="Foto de Andrey Tomaz Silva Alves" style="border-radius: 8px;"/><br>
        <sub>
          <b>ANDREY TOMAZ</b><br>
          <b>RA: 2400729</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

## 📎 Licença

Este projeto foi desenvolvido como parte de uma atividade avaliativa da disciplina de **RPA - Robotic Process Automation** e não possui fins comerciais.