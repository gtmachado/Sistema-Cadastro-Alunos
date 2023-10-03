import os
import sqlite3


nome_banco_dados = "db/cadastro.db"

nome_arquivo_sql = os.path.join(os.path.dirname(nome_banco_dados), "backup.sql")

conn = sqlite3.connect(nome_banco_dados)

cursor = conn.cursor()

with open(nome_arquivo_sql, "w") as arquivo_sql:
    for linha in conn.iterdump():
        arquivo_sql.write(f"{linha}\n")

conn.close()
