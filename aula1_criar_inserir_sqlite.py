# criação de tabela e inserção de dados sqlite

import sqlite3

banco = sqlite3.connect('primeiro_banco.db') # objeto de conexao com o banco

cursor = banco.cursor() # comando cursor serve para fazer as ações da tabela: criar, inserir, atualizar e deletar

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)") # criar tabela (comando para ser usado somente uma vez)

cursor.execute("INSERT INTO pessoas VALUES('Fernanda', 27, 'fernanda_123@gmail.com')") #inserir dados na tabela

banco.commit()

# cursor.execute("SELECT * FROM pessoas") #comando sql para ver todos os dados da tabela
# print(cursor.fetchall())