import sqlite3
import os

def criar_conexao():
    print("Banco sendo usado em:", os.path.abspath("meu_corinthians.db"))
    conexao = sqlite3.connect("meu_corinthians.db")
    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            numero INTEGER,
            posicao TEXT
        )
    """

    cursor.execute(sql)
    conexao.commit()
    conexao.close()

def inserir_jogadores():
    conexao = sqlite3.connect("meu_corinthians.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM jogadores")
    quantidade = cursor.fetchone()[0]

    if quantidade == 0:
        cursor.executemany("INSERT INTO jogadores (nome, numero, posicao) VALUES (?, ?, ?)", [
            # Goleiros
            ("Hugo Souza", 1, "Goleiro"),
            ("Felipe Longo", 40, "Goleiro"),
            ("Kauê", 51, "Goleiro"),
            # Zagueiros
            ("Gabriel Paulista", 3, "Zagueiro"),
            ("João Pedro", 4, "Zagueiro"),
            ("André Ramalho", 5, "Zagueiro"),
            ("Gustavo Henrique", 13, "Zagueiro"),
            # Laterais
            ("Matheuzinho", 2, "Lateral-direito"),
            ("Pedro Milans", 20, "Lateral-direito"),
            ("João Vitor", 59, "Lateral-direito"),
            ("Matheus Bidu", 21, "Lateral-esquerdo"),
            ("Fabrizio Angileri", 26, "Lateral-esquerdo"),
            ("Hugo Ferreira", 46, "Lateral-esquerdo"),
            # Volantes
            ("Raniele", 14, "Volante"),
            ("Matheus Pereira", 23, "Volante"),
            ("Allan", 29, "Volante"),
            ("Charles", 35, "Volante"),
            ("André", 49, "Volante"),
            ("Luiz Gustavo", 54, "Volante"),
            ("Alex Santana", 80, "Volante"),
            # Meias
            ("Breno Bidon", 7, "Meia"),
            ("Rodrigo Garro", 8, "Meia"),
            ("André Carrillo", 19, "Meia"),
            ("Gui Amorim", 48, "Meia"),
            ("Zakaria Labyad", 52, "Meia"),
            # Atacantes
            ("Yuri Alberto", 9, "Atacante"),
            ("Memphis Depay", 10, "Atacante"),
            ("Vitinho", 11, "Atacante"),
            ("Pedro Raul", 18, "Atacante"),
            ("Kayke", 31, "Atacante"),
            ("Kaio César", 37, "Atacante"),
            ("Gui Negão", 56, "Atacante"),
            ("Dieguinho", 61, "Atacante"),
            ("Jesse Lingard", 77, "Atacante")
        ])
    conexao.commit()
    conexao.close()

def listar_jogadores():
    conexao = sqlite3.connect("meu_corinthians.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, numero, posicao FROM jogadores")
    linhas = cursor.fetchall()
    jogadores = [dict(linha) for linha in linhas]

    conexao.close()

    return jogadores

def criar_tabela_favoritos():
    conexao = sqlite3.connect("meu_corinthians.db")
    cursor = conexao.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS favoritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jogador_id INTEGER
        )
    """

    cursor.execute(sql)
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_conexao()
    inserir_jogadores()
    criar_tabela_favoritos()

def adicionar_favorito(jogador_id):
    conexao = sqlite3.connect("meu_corinthians.db")
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO favoritos (jogador_id) VALUES (?)", (jogador_id,))
    conexao.commit()
    conexao.close()

def remover_favorito(jogador_id):
    conexao = sqlite3.connect("meu_corinthians.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM favoritos WHERE jogador_id = ?", (jogador_id,))
    conexao.commit()
    conexao.close()

def listar_favoritos():
    conexao = sqlite3.connect("meu_corinthians.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT jogador_id FROM favoritos
    """)
    linhas = cursor.fetchall()
    favoritos = [linha[0] for linha in linhas]

    conexao.close()

    return favoritos