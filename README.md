
<h1 align="center">📘 Projeto: Coleta de Dados de Países e Livros com Python</h1>

<p align="center">
  Projeto acadêmico da disciplina de RPA, desenvolvido para automatizar a extração de dados públicos sobre <strong>países</strong> e <strong>livros</strong>. As informações são armazenadas em bancos de dados SQLite e um relatório final em Excel é gerado.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/SQLite-integrado-lightgrey?logo=sqlite" />
  <img src="https://img.shields.io/badge/OpenPyXL-relatórios-green?logo=python" />
  <img src="https://img.shields.io/badge/BeautifulSoup-webscraping-orange?logo=beautifulsoup" />
</p>

---

<details>
  <summary><strong>🧠 Funcionalidades</strong></summary>

### 🔹 Parte 1 – API REST (REST Countries)
- Solicita o nome de **3 países** ao usuário.
- Consulta a [REST Countries API](https://restcountries.com/).
- Armazena as informações em um banco SQLite: `paises.db`.

### 🔹 Parte 2 – Web Scraping (Books to Scrape)
- Acessa o site [Books to Scrape](http://books.toscrape.com/).
- Coleta os **10 primeiros livros**, extraindo:
  - Título
  - Preço
  - Avaliação
  - Disponibilidade
- Armazena os dados em `livraria.db`.

### 🔹 Parte 3 – Geração de Relatório
- Cria um arquivo Excel: `relatorio_final.xlsx`
- O relatório contém:
  - Dados dos países e livros coletados
  - Nome dos autores
  - Data da execução

</details>

---

<details>
  <summary><strong>⚙️ Tecnologias Utilizadas</strong></summary>

- **Python 3.x**
- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
- [`openpyxl`](https://pypi.org/project/openpyxl/)
- `sqlite3` (biblioteca padrão do Python)

</details>

---

<details>
  <summary><strong>🚀 Como Executar o Projeto</strong></summary>

### 🔁 Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-paises-livros-python.git
cd projeto-paises-livros-python
```

### 📦 Instale as dependências:
```bash
pip install requests beautifulsoup4 openpyxl
```

### ▶️ Execute o script principal:
```bash
python projeto_final.py
```

> 💡 Será solicitado que você digite o nome de 3 países.

Após a execução, os seguintes arquivos serão gerados automaticamente:
- `paises.db`
- `livraria.db`
- `relatorio_final.xlsx`

</details>

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
