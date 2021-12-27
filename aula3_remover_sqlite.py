# remoção de um dado sqlite

import sqlite3

try:

    banco = sqlite3.connect('primeiro_banco.db') # objeto de conexao com o banco

    cursor = banco.cursor()

    cursor.execute("DELETE from pessoas WHERE idade = 12") # deletar dados

    banco.commit()
    banco.close()
    print("Os dados foram removidos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)