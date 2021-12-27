# criação de tabela e inserção de dados através de variáveis sqlite

import sqlite3

nome = "Juliana"
idade = 28
email = "juliana@gmail.com"

banco = sqlite3.connect('primeiro_banco.db') # objeto de conexao com o banco

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")

banco.commit()