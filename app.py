import requests
import sqlite3
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

def extrair_dados_paises(paises):
    dados = []
    for pais in paises:
        print(f"🔎 Buscando dados do país: {pais}")
        response = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
        if response.status_code == 200:
            info = response.json()[0]
            nome_comum = info['name']['common']
            nome_oficial = info['name']['official']
            capital = info.get('capital', ['Desconhecida'])[0]
            continente = info.get('continents', ['Desconhecido'])[0]
            regiao = info.get('region', 'Desconhecida')
            subregiao = info.get('subregion', 'Desconhecida')
            populacao = info.get('population', 0)
            area = info.get('area', 0.0)
            moeda_chave = list(info['currencies'].keys())[0]
            moeda_nome = info['currencies'][moeda_chave]['name']
            moeda_simbolo = info['currencies'][moeda_chave].get('symbol', '')
            idioma = list(info['languages'].values())[0]
            fuso = ', '.join(info.get('timezones', []))
            bandeira = info['flags']['png']
            dados.append((nome_comum, nome_oficial, capital, continente, regiao, subregiao,
                          populacao, area, moeda_nome, moeda_simbolo, idioma, fuso, bandeira))
        else:
            print(f"⚠️ Não foi possível encontrar dados para: {pais}")
    return dados

def salvar_dados_sqlite_paises(dados):
    conn = sqlite3.connect('paises.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS paises (
            nome_comum TEXT, nome_oficial TEXT, capital TEXT, continente TEXT, 
            regiao TEXT, subregiao TEXT, populacao INTEGER, area REAL, 
            moeda TEXT, simbolo TEXT, idioma TEXT, fuso TEXT, bandeira TEXT
        )
    """)
    c.executemany('INSERT INTO paises VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', dados)
    conn.commit()
    conn.close()

def coletar_livros():
    print("\n📚 Coletando dados dos 10 primeiros livros do site...")
    url = "https://books.toscrape.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    livros = soup.select("article.product_pod")[:10]

    resultado = []
    for livro in livros:
        titulo = livro.h3.a["title"]
        preco = livro.select_one(".price_color").text.replace("£", "")
        estrelas = livro.p.get("class")[1]
        disponibilidade = livro.select_one(".availability").text.strip()
        resultado.append((titulo, preco, estrelas, disponibilidade))
    return resultado

def salvar_livros_sqlite(dados):
    conn = sqlite3.connect("livraria.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            titulo TEXT, preco TEXT, avaliacao TEXT, disponibilidade TEXT
        )
    """)
    c.executemany("INSERT INTO livros VALUES (?,?,?,?)", dados)
    conn.commit()
    conn.close()

def gerar_relatorio_excel(nome_aluno):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Países"

    conn = sqlite3.connect('paises.db')
    c = conn.cursor()
    c.execute("SELECT * FROM paises")
    dados_paises = c.fetchall()
    colunas_paises = [desc[0] for desc in c.description]
    ws1.append(colunas_paises)
    for linha in dados_paises:
        ws1.append(linha)

    ws2 = wb.create_sheet(title="Livros")
    conn = sqlite3.connect('livraria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM livros")
    dados_livros = c.fetchall()
    colunas_livros = [desc[0] for desc in c.description]
    ws2.append(colunas_livros)
    for linha in dados_livros:
        ws2.append(linha)

    ws2.append([])
    ws2.append(["Relatório gerado por:", nome_aluno])
    ws2.append(["Data de geração:", datetime.now().strftime("%d/%m/%Y %H:%M")])
    
    wb.save("relatorio_final.xlsx")

if __name__ == "__main__":
    print("🌍 Bem-vindo! Vamos buscar informações de 3 países.")
    paises = []
    for i in range(3):
        pais = input(f"Digite o nome do {i+1}º país: ")
        paises.append(pais.strip())

    dados_paises = extrair_dados_paises(paises)
    salvar_dados_sqlite_paises(dados_paises)

    dados_livros = coletar_livros()
    salvar_livros_sqlite(dados_livros)

    gerar_relatorio_excel("Andrey | Henry")
    print("\n✅ Projeto finalizado com sucesso! Arquivo relatorio_final.xlsx gerado.")
    input("\nPressione ENTER para sair.")
