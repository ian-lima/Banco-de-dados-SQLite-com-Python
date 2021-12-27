# atualizar dados sqlite

import sqlite3

nome = "Juliana"
idade = 28
email = "juliana@gmail.com"

banco = sqlite3.connect('primeiro_banco.db') # objeto de conexao com o banco

cursor = banco.cursor() 

cursor.execute("UPDATE pessoas SET nome = 'Fabio' WHERE idade = 28")

banco.commit()